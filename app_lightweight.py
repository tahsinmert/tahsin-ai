from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import json
import re
import os
import gc

app = Flask(__name__)
CORS(app)

# Memory optimizasyonu
torch.set_grad_enabled(False)
torch.backends.cudnn.benchmark = False

# Sadece bir model yükle (memory tasarrufu için)
print("Hafif model yükleniyor...")

try:
    from transformers import AutoModelForCausalLM, AutoTokenizer
    
    # En hafif model: DialoGPT-small
    print("DialoGPT-small modeli yükleniyor...")
    model_name = "microsoft/DialoGPT-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True,
        device_map='auto'
    )
    
    # PAD token ayarla
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    
    print("Model başarıyla yüklendi!")
    MODEL_LOADED = True
    
except Exception as e:
    print(f"Model yükleme hatası: {e}")
    MODEL_LOADED = False

def create_prompt(user_input):
    """Basit prompt oluşturma"""
    return f"User: {user_input}\nAssistant:"

def post_process_response(response):
    """Yanıtı temizle ve formatla"""
    # Assistant: kısmını al
    if "Assistant:" in response:
        response = response.split("Assistant:")[-1].strip()
    
    # Temizle
    response = re.sub(r'\s+', ' ', response)
    response = response.strip()
    
    # Kısa yanıtları uzat
    if len(response) < 50:
        response += " Bu konuda daha fazla bilgi almak isterseniz, lütfen sorunuzu detaylandırabilirsiniz."
    
    return response

@app.route('/api/generate', methods=['POST'])
def generate_response():
    if not MODEL_LOADED:
        return jsonify({'error': 'Model yüklenemedi'}), 500
    
    try:
        data = request.get_json()
        user_input = data.get('message', '')
        model_choice = data.get('model', 'dialogpt-small')

        if not user_input:
            return jsonify({'error': 'Mesaj boş olamaz'}), 400

        # Prompt oluştur
        prompt = create_prompt(user_input)
        
        # Tokenize et
        inputs = tokenizer.encode(prompt, return_tensors='pt', truncation=True, max_length=256)
        
        # Model çıktısını üret
        with torch.no_grad():
            outputs = model.generate(
                inputs,
                max_length=200,  # Daha kısa yanıtlar
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                top_p=0.9,
                top_k=50,
                repetition_penalty=1.1,
                pad_token_id=tokenizer.eos_token_id,
                eos_token_id=tokenizer.eos_token_id
            )
        
        # Çıktıyı decode et
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = post_process_response(generated_text)
        
        # Memory temizle
        del inputs, outputs
        gc.collect()
        torch.cuda.empty_cache() if torch.cuda.is_available() else None
        
        return jsonify({
            'answer': response,
            'source': {
                'url': '',
                'title': 'DialoGPT-small Model (Hafif)'
            },
            'searchEngine': 'DialoGPT-small (Hafif)'
        })
        
    except Exception as e:
        print(f"Yanıt üretme hatası: {str(e)}")
        return jsonify({'error': 'Yanıt üretirken hata oluştu'}), 500

@app.route('/api/models', methods=['GET'])
def get_available_models():
    return jsonify({
        'models': [
            {
                'id': 'dialogpt-small',
                'name': 'DialoGPT-small (Hafif)',
                'description': 'Hafif İngilizce sohbet modeli - Microsoft (Memory Optimized)',
                'language': 'İngilizce'
            }
        ]
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy' if MODEL_LOADED else 'error',
        'models': ['DialoGPT-small (Hafif)'] if MODEL_LOADED else [],
        'active_models': 1 if MODEL_LOADED else 0,
        'features': ['Memory Optimized', 'Lightweight Model', 'Fast Response']
    })

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Tahsin AI Hafif Backend',
        'status': 'running',
        'model_loaded': MODEL_LOADED
    })

if __name__ == '__main__':
    print("Tahsin AI Hafif Backend başlatılıyor...")
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug) 