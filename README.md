# Tahsin AI - VIP Çoklu Model Destekli Akıllı Asistan

✨ **Tahsin Mert MUTLU** tarafından kodlanmış gelişmiş AI asistanı.

## 🚀 Özellikler

### 🤖 **Çoklu AI Model Desteği**
- **Turkish GPT-2**: Türkçe dil modeli (YTU-CE-Cosmos)
- **DialoGPT-medium**: İngilizce sohbet modeli (Microsoft)
- **Flan-T5-base**: Çok dilli güçlü AI modeli (Google)

### 🎨 **Modern VIP Tasarım**
- Glassmorphism UI
- Neon efektler
- Animasyonlu arka plan
- Responsive tasarım
- Mobile-first yaklaşım

### 🎤 **Ses Özellikleri**
- AI sesli yanıt
- Sesli soru sorma
- Otomatik dil tespiti
- Web Speech API entegrasyonu

### 🧠 **Gelişmiş AI Özellikleri**
- Advanced Prompt Engineering
- Question Type Analysis
- Response Post-Processing
- Enhanced Parameters
- Automatic Translation

## 🛠️ Teknolojiler

### Frontend
- **HTML5**: Modern semantic markup
- **CSS3**: Glassmorphism, animations, responsive design
- **JavaScript (ES6+)**: Web Speech API, async/await, modern JS features

### Backend
- **Python**: Serverless functions
- **Transformers**: Hugging Face AI models
- **PyTorch**: Deep learning framework
- **Vercel**: Serverless deployment

## 📱 Responsive Tasarım

- **Desktop**: Tam özellikli VIP deneyim
- **Tablet**: Optimize edilmiş arayüz
- **Mobile**: Tam ekran, scroll bar yok
- **All Devices**: Mükemmel uyumluluk

## 🚀 Deployment

### Vercel ile Deploy

1. **Repository'yi klonlayın:**
```bash
git clone <repository-url>
cd tahsin-ai
```

2. **Vercel CLI kurun:**
```bash
npm i -g vercel
```

3. **Deploy edin:**
```bash
vercel
```

4. **Production'a deploy edin:**
```bash
vercel --prod
```

### Manuel Deploy

1. **Vercel Dashboard'a gidin**
2. **"New Project" seçin**
3. **GitHub repository'nizi bağlayın**
4. **Deploy edin**

## 📁 Proje Yapısı

```
tahsin-ai/
├── index.html              # Ana frontend dosyası
├── vercel.json             # Vercel konfigürasyonu
├── requirements.txt        # Python dependencies
├── api/
│   └── generate.py         # Serverless API endpoint
└── README.md              # Bu dosya
```

## 🔧 API Endpoints

### POST `/api/generate`
AI yanıtı üretir.

**Request:**
```json
{
  "message": "Merhaba, nasılsın?",
  "model": "turkish-gpt2"
}
```

**Response:**
```json
{
  "answer": "Merhaba! Ben çok iyiyim, teşekkür ederim. Size nasıl yardımcı olabilirim?",
  "searchEngine": "Turkish GPT-2 (Gelişmiş)",
  "source": {
    "title": "Turkish GPT-2 Model (Gelişmiş)",
    "url": ""
  }
}
```

### GET `/api/health`
Backend sağlık kontrolü.

### GET `/api/models`
Mevcut modelleri listeler.

## 🎯 Kullanım

1. **Model Seçin**: Dropdown'dan istediğiniz AI modelini seçin
2. **Ses Ayarları**: AI sesli yanıt ve sesli soru özelliklerini aktifleştirin
3. **Soru Sorun**: Metin kutusuna sorunuzu yazın veya sesli sorun
4. **Yanıt Alın**: AI modelinizden gelişmiş yanıt alın

## 🌟 Özellikler

### 🎨 **VIP Tasarım**
- Modern glassmorphism efektleri
- Neon ışık efektleri
- Animasyonlu arka plan
- Floating particles
- Shimmer animasyonları

### 🧠 **AI Modelleri**
- **Turkish GPT-2**: Türkçe konuşmalar için optimize
- **DialoGPT-medium**: İngilizce sohbetler için
- **Flan-T5-base**: Çok dilli destek + otomatik çeviri

### 🎤 **Ses Özellikleri**
- AI yanıtlarını sesli dinleme
- Sesli soru sorma
- Otomatik dil tespiti
- Türkçe ve İngilizce ses desteği

### 📱 **Mobile Optimizasyon**
- Tam ekran deneyim
- Scroll bar yok
- Touch-friendly tasarım
- Responsive layout

## 🔮 Gelecek Özellikler

- [ ] Daha fazla AI modeli
- [ ] Görsel AI özellikleri
- [ ] Dosya yükleme desteği
- [ ] Çoklu kullanıcı desteği
- [ ] Gelişmiş analitikler

## 📞 İletişim

**Geliştirici:** Tahsin Mert MUTLU

---

⭐ **Bu proje açık kaynak kodludur ve eğitim amaçlı geliştirilmiştir.** 