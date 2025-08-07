from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import GPT2LMHeadModel, GPT2Tokenizer, AutoModelForCausalLM, AutoTokenizer, T5ForConditionalGeneration, T5Tokenizer
import torch
import json
import re
import os

app = Flask(__name__)
CORS(app)

# Modelleri yükle
print("Modeller yükleniyor...")

# Turkish GPT-2 modeli
print("Turkish GPT-2 modeli yükleniyor...")
turkish_model_name = "ytu-ce-cosmos/turkish-gpt2"
turkish_tokenizer = GPT2Tokenizer.from_pretrained(turkish_model_name)
turkish_model = GPT2LMHeadModel.from_pretrained(turkish_model_name)

# PAD token'ı ayarla
if turkish_tokenizer.pad_token is None:
    turkish_tokenizer.pad_token = turkish_tokenizer.eos_token

# DialoGPT-medium modeli
print("DialoGPT-medium modeli yükleniyor...")
dialogpt_model_name = "microsoft/DialoGPT-medium"
dialogpt_tokenizer = AutoTokenizer.from_pretrained(dialogpt_model_name)
dialogpt_model = AutoModelForCausalLM.from_pretrained(dialogpt_model_name)

# PAD token'ı ayarla
if dialogpt_tokenizer.pad_token is None:
    dialogpt_tokenizer.pad_token = dialogpt_tokenizer.eos_token

# Flan-T5-base modeli
print("Flan-T5-base modeli yükleniyor...")
flan_t5_model_name = "google/flan-t5-base"
flan_t5_tokenizer = T5Tokenizer.from_pretrained(flan_t5_model_name)
flan_t5_model = T5ForConditionalGeneration.from_pretrained(flan_t5_model_name)

print("Tüm modeller başarıyla yüklendi!")

def create_advanced_prompt(user_input, model_type):
    """Gelişmiş prompt oluşturma fonksiyonu"""
    
    # Soru türünü analiz et
    question_type = analyze_question_type(user_input)
    
    if model_type == "turkish-gpt2":
        if question_type == "technical":
            return f"""Aşağıdaki teknik soruyu detaylı ve kapsamlı bir şekilde yanıtla. Bilimsel terimleri açıkla ve pratik örnekler ver:

Soru: {user_input}

Tahsin AI: Bu konuda size detaylı bir açıklama yapayım. """
        
        elif question_type == "general":
            return f"""Aşağıdaki genel soruyu kapsamlı ve anlaşılır bir şekilde yanıtla. Farklı açılardan ele al ve örneklerle destekle:

Soru: {user_input}

Tahsin AI: Bu konu hakkında size kapsamlı bilgi vereyim. """
        
        elif question_type == "creative":
            return f"""Aşağıdaki yaratıcı soruyu ilham verici ve detaylı bir şekilde yanıtla. Farklı perspektifler sun ve pratik öneriler ver:

Soru: {user_input}

Tahsin AI: Bu konuda size ilham verici bir yanıt vereyim. """
        
        else:
            return f"""Aşağıdaki soruyu detaylı, kapsamlı ve mantıklı bir şekilde yanıtla. Bilimsel gerçekleri, pratik örnekleri ve farklı açıları dahil et:

Soru: {user_input}

Tahsin AI: Bu konuda size kapsamlı bir açıklama yapayım. """
    
    elif model_type == "dialogpt-medium":
        if question_type == "technical":
            return f"""Please provide a comprehensive and detailed answer to this technical question. Explain scientific concepts clearly and provide practical examples:

Question: {user_input}

Answer: Let me provide you with a detailed explanation of this topic. """
        
        elif question_type == "general":
            return f"""Please give a thorough and well-structured answer to this general question. Consider multiple perspectives and provide relevant examples:

Question: {user_input}

Answer: Let me give you a comprehensive response to this question. """
        
        else:
            return f"""Please provide a detailed, logical, and well-reasoned answer to this question. Include scientific facts, practical examples, and different perspectives:

Question: {user_input}

Answer: Let me provide you with a comprehensive explanation. """
    
    elif model_type == "flan-t5-base":
        if question_type == "technical":
            return f"""Provide a comprehensive technical explanation with detailed analysis, scientific background, and practical applications:

Question: {user_input}

Answer: """
        
        elif question_type == "general":
            return f"""Give a thorough and well-structured response with multiple perspectives, examples, and detailed analysis:

Question: {user_input}

Answer: """
        
        else:
            return f"""Provide a detailed, logical, and comprehensive answer with scientific facts, practical examples, and multiple viewpoints:

Question: {user_input}

Answer: """

def analyze_question_type(user_input):
    """Soru türünü analiz et"""
    input_lower = user_input.lower()
    
    # Teknik terimler
    technical_keywords = ['python', 'javascript', 'programming', 'algorithm', 'database', 'api', 'framework', 
                         'machine learning', 'ai', 'artificial intelligence', 'neural network', 'deep learning',
                         'quantum', 'physics', 'chemistry', 'biology', 'mathematics', 'engineering', 'technology',
                         'software', 'hardware', 'network', 'security', 'cloud', 'blockchain', 'cryptocurrency']
    
    # Yaratıcı terimler
    creative_keywords = ['story', 'creative', 'imagine', 'design', 'art', 'music', 'poetry', 'novel', 'fiction',
                        'inspiration', 'idea', 'concept', 'vision', 'dream', 'fantasy', 'adventure']
    
    # Genel terimler
    general_keywords = ['what is', 'how to', 'why', 'when', 'where', 'who', 'explain', 'describe', 'tell me about',
                       'information', 'knowledge', 'learn', 'understand', 'help', 'guide']
    
    for keyword in technical_keywords:
        if keyword in input_lower:
            return "technical"
    
    for keyword in creative_keywords:
        if keyword in input_lower:
            return "creative"
    
    for keyword in general_keywords:
        if keyword in input_lower:
            return "general"
    
    return "general"

def post_process_response(response, model_type):
    """Yanıtı işle ve geliştir"""
    
    # Boş yanıtları kontrol et
    if not response or len(response.strip()) < 10:
        return "Üzgünüm, bu konuda yeterli bilgi üretemedim. Lütfen sorunuzu farklı şekilde ifade edebilir misiniz?"
    
    # Yanıtı temizle
    response = response.strip()
    
    # Çok kısa yanıtları genişlet
    if len(response) < 50:
        if model_type == "turkish-gpt2":
            response += " Bu konuda daha fazla bilgi almak isterseniz, lütfen sorunuzu detaylandırabilirsiniz."
        else:
            response += " For more information on this topic, please feel free to ask follow-up questions."
    
    # Yanıtı yapılandır
    if model_type == "turkish-gpt2":
        # Türkçe yanıtları yapılandır
        if not response.endswith(('.', '!', '?')):
            response += '.'
        
        # Paragrafları düzenle
        response = re.sub(r'\n+', '\n\n', response)
        
    else:
        # İngilizce yanıtları yapılandır
        if not response.endswith(('.', '!', '?')):
            response += '.'
        
        # Paragrafları düzenle
        response = re.sub(r'\n+', '\n\n', response)
    
    return response

@app.route('/api/generate', methods=['POST'])
def generate_response():
    try:
        data = request.get_json()
        user_input = data.get('message', '')
        model_choice = data.get('model', 'turkish-gpt2')  # Varsayılan Turkish GPT-2
        
        if not user_input:
            return jsonify({'error': 'Mesaj boş olamaz'}), 400
        
        if model_choice == 'turkish-gpt2':
            return generate_turkish_gpt2_response(user_input)
        elif model_choice == 'dialogpt-medium':
            return generate_dialogpt_response(user_input)
        elif model_choice == 'flan-t5-base':
            return generate_flan_t5_response(user_input)
        else:
            return jsonify({'error': 'Geçersiz model seçimi'}), 400
        
    except Exception as e:
        print(f"Hata: {str(e)}")
        return jsonify({'error': 'Model yanıt üretirken hata oluştu'}), 500

def generate_turkish_gpt2_response(user_input):
    try:
        # Gelişmiş prompt oluştur
        prompt = create_advanced_prompt(user_input, "turkish-gpt2")
        
        # Tokenize et
        inputs = turkish_tokenizer.encode(prompt, return_tensors='pt', truncation=True, max_length=512)
        
        # Model çıktısını üret (gelişmiş parametreler)
        with torch.no_grad():
            outputs = turkish_model.generate(
                inputs,
                max_length=400,  # Daha uzun yanıtlar
                num_return_sequences=1,
                temperature=0.8,  # Daha yaratıcı
                do_sample=True,
                top_p=0.9,  # Nucleus sampling
                top_k=50,  # Top-k sampling
                repetition_penalty=1.2,  # Tekrarları önle
                length_penalty=1.0,  # Uzunluk cezası
                pad_token_id=turkish_tokenizer.eos_token_id,
                eos_token_id=turkish_tokenizer.eos_token_id,
                early_stopping=True
            )
        
        # Çıktıyı decode et
        generated_text = turkish_tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Sadece AI yanıtını al
        response = generated_text.split("Tahsin AI:")[-1].strip()
        
        # Yanıtı işle
        response = post_process_response(response, "turkish-gpt2")
        
        return jsonify({
            'answer': response,
            'source': {
                'url': '',
                'title': 'Turkish GPT-2 Model (Gelişmiş)'
            },
            'searchEngine': 'Turkish GPT-2 (Gelişmiş)'
        })
        
    except Exception as e:
        print(f"Turkish GPT-2 hatası: {str(e)}")
        return jsonify({'error': 'Turkish GPT-2 modeli yanıt üretirken hata oluştu'}), 500

def generate_dialogpt_response(user_input):
    try:
        # Gelişmiş prompt oluştur
        prompt = create_advanced_prompt(user_input, "dialogpt-medium")
        
        # Kullanıcı girişini tokenize et
        inputs = dialogpt_tokenizer.encode(prompt + dialogpt_tokenizer.eos_token, return_tensors='pt')
        
        # Model çıktısını üret (gelişmiş parametreler)
        with torch.no_grad():
            outputs = dialogpt_model.generate(
                inputs,
                max_length=400,  # Daha uzun yanıtlar
                num_return_sequences=1,
                temperature=0.8,  # Daha yaratıcı
                do_sample=True,
                top_p=0.9,  # Nucleus sampling
                top_k=50,  # Top-k sampling
                repetition_penalty=1.2,  # Tekrarları önle
                length_penalty=1.0,  # Uzunluk cezası
                pad_token_id=dialogpt_tokenizer.eos_token_id,
                eos_token_id=dialogpt_tokenizer.eos_token_id,
                early_stopping=True
            )
        
        # Çıktıyı decode et
        response = dialogpt_tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
        
        # Yanıtı işle
        response = post_process_response(response, "dialogpt-medium")
        
        return jsonify({
            'answer': response,
            'source': {
                'url': '',
                'title': 'DialoGPT-medium Model (Gelişmiş)'
            },
            'searchEngine': 'DialoGPT-medium (Gelişmiş)'
        })
        
    except Exception as e:
        print(f"DialoGPT hatası: {str(e)}")
        return jsonify({'error': 'DialoGPT modeli yanıt üretirken hata oluştu'}), 500

def generate_flan_t5_response(user_input):
    try:
        # Gelişmiş prompt oluştur
        prompt = create_advanced_prompt(user_input, "flan-t5-base")
        
        # Tokenize et
        inputs = flan_t5_tokenizer.encode(prompt, return_tensors='pt', truncation=True, max_length=512)
        
        # Model çıktısını üret (gelişmiş parametreler)
        with torch.no_grad():
            outputs = flan_t5_model.generate(
                inputs,
                max_length=400,  # Daha uzun yanıtlar
                num_return_sequences=1,
                temperature=0.8,  # Daha yaratıcı
                do_sample=True,
                top_p=0.9,  # Nucleus sampling
                top_k=50,  # Top-k sampling
                repetition_penalty=1.2,  # Tekrarları önle
                length_penalty=1.0,  # Uzunluk cezası
                early_stopping=True
            )
        
        # Çıktıyı decode et
        response = flan_t5_tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Yanıtı işle
        response = post_process_response(response, "flan-t5-base")
        
        return jsonify({
            'answer': response,
            'source': {
                'url': '',
                'title': 'Flan-T5-base Model (Gelişmiş)'
            },
            'searchEngine': 'Flan-T5-base (Gelişmiş)'
        })
        
    except Exception as e:
        print(f"Flan-T5 hatası: {str(e)}")
        return jsonify({'error': 'Flan-T5 modeli yanıt üretirken hata oluştu'}), 500

@app.route('/api/models', methods=['GET'])
def get_available_models():
    return jsonify({
        'models': [
            {
                'id': 'turkish-gpt2',
                'name': 'Turkish GPT-2 (Gelişmiş)',
                'description': 'Türkçe dil modeli - YTU-CE-Cosmos (Gelişmiş Prompt Engineering)',
                'language': 'Türkçe'
            },
            {
                'id': 'dialogpt-medium',
                'name': 'DialoGPT-medium (Gelişmiş)',
                'description': 'İngilizce sohbet modeli - Microsoft (Gelişmiş Prompt Engineering)',
                'language': 'İngilizce'
            },
            {
                'id': 'flan-t5-base',
                'name': 'Flan-T5-base (Gelişmiş)',
                'description': 'Çok dilli güçlü AI modeli - Google (Gelişmiş Prompt Engineering)',
                'language': 'Çok Dilli'
            }
        ]
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy', 
        'models': ['Turkish GPT-2 (Gelişmiş)', 'DialoGPT-medium (Gelişmiş)', 'Flan-T5-base (Gelişmiş)'],
        'active_models': 3,
        'features': ['Advanced Prompt Engineering', 'Question Type Analysis', 'Response Post-Processing', 'Enhanced Parameters']
    })

if __name__ == '__main__':
    print("Tahsin AI Gelişmiş Çoklu Model Backend başlatılıyor...")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 