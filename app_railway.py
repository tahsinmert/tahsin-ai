from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import time

app = Flask(__name__)
CORS(app)

# Basit mock AI yanıtları (model yüklemeden)
MOCK_RESPONSES = {
    "merhaba": "Merhaba! Ben Tahsin AI'nın hafif versiyonuyum. Size nasıl yardımcı olabilirim?",
    "nasılsın": "Teşekkürler, ben iyiyim! Railway'de çalışıyorum ve size yardımcı olmaya hazırım.",
    "yapay zeka": "Yapay zeka, bilgisayarların insan benzeri düşünme ve öğrenme yeteneklerine sahip olmasını sağlayan teknolojidir.",
    "python": "Python, öğrenmesi kolay ve güçlü bir programlama dilidir. Web geliştirme, veri analizi ve AI alanlarında yaygın kullanılır.",
    "default": "Bu konuda size yardımcı olmaya çalışıyorum. Daha detaylı bilgi için sorunuzu genişletebilir misiniz?"
}

def get_mock_response(user_input):
    """Basit keyword-based yanıt sistemi"""
    user_input_lower = user_input.lower()
    
    for keyword, response in MOCK_RESPONSES.items():
        if keyword in user_input_lower:
            return response
    
    return MOCK_RESPONSES["default"]

@app.route('/api/generate', methods=['POST'])
def generate_response():
    try:
        data = request.get_json()
        user_input = data.get('message', '')
        model_choice = data.get('model', 'mock-ai')

        if not user_input:
            return jsonify({'error': 'Mesaj boş olamaz'}), 400

        # Basit yanıt üret
        response = get_mock_response(user_input)
        
        # Kısa bir gecikme (gerçek AI simülasyonu)
        time.sleep(0.5)
        
        return jsonify({
            'answer': response,
            'source': {
                'url': '',
                'title': 'Mock AI (Railway Optimized)'
            },
            'searchEngine': 'Mock AI (Railway Optimized)'
        })
        
    except Exception as e:
        print(f"Yanıt üretme hatası: {str(e)}")
        return jsonify({'error': 'Yanıt üretirken hata oluştu'}), 500

@app.route('/api/models', methods=['GET'])
def get_available_models():
    return jsonify({
        'models': [
            {
                'id': 'mock-ai',
                'name': 'Mock AI (Railway Optimized)',
                'description': 'Hafif mock AI sistemi - Railway için optimize edilmiş',
                'language': 'Türkçe/İngilizce'
            }
        ]
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'models': ['Mock AI (Railway Optimized)'],
        'active_models': 1,
        'features': ['Railway Optimized', 'Fast Response', 'No Memory Issues'],
        'timestamp': time.time()
    })

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Tahsin AI Railway Backend',
        'status': 'running',
        'version': 'railway-optimized',
        'timestamp': time.time()
    })

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({
        'message': 'API çalışıyor!',
        'status': 'success'
    })

if __name__ == '__main__':
    print("Tahsin AI Railway Backend başlatılıyor...")
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug) 