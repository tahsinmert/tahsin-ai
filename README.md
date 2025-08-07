# 🤖 Tahsin AI - Turkish GPT-2 Destekli Akıllı Asistan

✨ **VIP Çoklu Model Destekli Akıllı Asistan** ✨

## 🚀 Özellikler

### 🎯 **AI Modelleri**
- 🤖 **Turkish GPT-2**: YTU-CE-Cosmos tarafından geliştirilmiş Türkçe dil modeli
- 💬 **DialoGPT-medium**: Microsoft'un İngilizce sohbet modeli
- 🚀 **Flan-T5-base**: Google'ın çok dilli güçlü AI modeli

### 🎨 **Modern Arayüz**
- ✨ **VIP Tasarım**: Glassmorphism ve neon efektler
- 📱 **Responsive**: Tüm cihazlarda mükemmel görünüm
- 🎭 **Animasyonlar**: Floating particles, shimmer, pulse efektleri
- 🌈 **Gradient Renkler**: Cyan, magenta, orange, gold renk paleti

### 🎤 **Ses Özellikleri**
- 🔊 **AI Sesli Yanıt**: Tüm modellerin yanıtları sesli okunur
- 🎤 **Sesli Soru**: Mikrofon ile sesli soru sorma
- 🌍 **Çok Dilli**: Otomatik dil algılama ve çeviri

### 🧠 **Gelişmiş AI**
- 🎯 **Prompt Engineering**: Gelişmiş prompt mühendisliği
- 🔍 **Soru Analizi**: Teknik, genel, yaratıcı soru türü analizi
- ✨ **Yanıt İşleme**: Otomatik temizleme ve formatlama
- ⚡ **Hızlı Yanıt**: Optimize edilmiş parametreler

## 📋 Gereksinimler

### 🐍 **Python Versiyonu**
- Python 3.9.6 (test edildi)
- Python 3.8 veya üzeri (önerilen)

### 💻 **Sistem Gereksinimleri**
- **RAM**: Minimum 4GB (önerilen 8GB+)
- **Disk**: Minimum 2GB boş alan
- **GPU**: Opsiyonel (CUDA destekli)

### 🖥️ **Test Edilen Sistem**
- **OS**: macOS 24.6.0 (Darwin Kernel)
- **Architecture**: ARM64 (Apple Silicon)
- **Python**: 3.9.6
- **Pip**: 21.2.4

## 🛠️ Kurulum

### 1️⃣ **Projeyi İndirin**
```bash
git clone <repository-url>
cd tahsin-ai
```

### 2️⃣ **Sanal Ortam Oluşturun**
```bash
# Virtual environment oluştur
python3 -m venv venv

# Sanal ortamı aktifleştir
# macOS/Linux:
source venv/bin/activate
# Windows:
# venv\Scripts\activate
```

### 3️⃣ **Bağımlılıkları Yükleyin**

#### **Apple Silicon (M1/M2/M3) için:**
```bash
# Önce PyTorch'u Apple Silicon için yükle
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Sonra diğer paketleri yükle
pip install -r requirements.txt
```

#### **Intel Mac/Linux/Windows için:**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Modelleri İndirin**
```bash
# Backend'i başlat (modeller otomatik indirilir)
python3 app.py
```

## 🚀 Çalıştırma

### 1️⃣ **Backend Sunucusu**
```bash
# Terminal 1'de backend'i başlat
python3 app.py
```
Backend `http://localhost:5000` adresinde çalışacak.

### 2️⃣ **Frontend Sunucusu**
```bash
# Terminal 2'de frontend'i başlat
python3 -m http.server 8000
```
Frontend `http://localhost:8000` adresinde çalışacak.

### 3️⃣ **Tarayıcıda Açın**
```
http://localhost:8000
```

## 📱 Kullanım

### 🎛️ **Model Seçimi**
1. Üst kısımdaki dropdown'dan istediğiniz AI modelini seçin
2. Her model farklı dil ve yeteneklere sahiptir

### 🎤 **Ses Özellikleri**
1. **AI Sesli Yanıt**: AI yanıtlarının sesli okunması için aktifleştirin
2. **Sesli Soru**: Mikrofon butonu ile sesli soru sorun

### 💬 **Sohbet**
1. Alt kısımdaki textarea'ya sorunuzu yazın
2. Enter tuşuna basın veya gönder butonuna tıklayın
3. AI modeliniz seçtiğiniz modele göre yanıt verecek

## 🏗️ Proje Yapısı

```
tahsin-ai/
├── index.html          # Ana frontend dosyası
├── app.py              # Flask backend sunucusu
├── requirements.txt    # Python bağımlılıkları
├── README.md          # Bu dosya
└── venv/              # Sanal ortam (oluşturulur)
```

## 🔧 API Endpoints

### 🏥 **Health Check**
```
GET /api/health
```
Backend durumunu kontrol eder.

### 🤖 **Model Listesi**
```
GET /api/models
```
Kullanılabilir AI modellerini listeler.

### 💬 **Yanıt Üretme**
```
POST /api/generate
Content-Type: application/json

{
    "message": "Merhaba, nasılsın?",
    "model": "turkish-gpt2"
}
```

## 🎨 Özelleştirme

### 🌈 **Renk Teması**
`index.html` dosyasındaki CSS değişkenlerini düzenleyin:
```css
:root {
    --primary-color: #00d4ff;    /* Ana renk */
    --secondary-color: #ff0080;  /* İkincil renk */
    --accent-color: #ff6b35;     /* Vurgu rengi */
    --gold-color: #ffd700;       /* Altın rengi */
}
```

### 🎭 **Animasyonlar**
CSS animasyonlarını `index.html` dosyasında düzenleyin:
- `backgroundShift`: Arka plan animasyonu
- `float`: Floating particles
- `shimmer`: Parlama efekti
- `vipPulse`: VIP pulse animasyonu

## 🐛 Sorun Giderme

### ❌ **Port Hatası**
```bash
# Port 5000 veya 8000 kullanımdaysa
lsof -ti:5000 | xargs kill -9
lsof -ti:8000 | xargs kill -9
```

### 📦 **Paket Hatası**

#### **Apple Silicon (M1/M2/M3) için:**
```bash
# Sanal ortamı yeniden oluştur
rm -rf venv
python3 -m venv venv
source venv/bin/activate

# Önce PyTorch'u Apple Silicon için yükle
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Sonra diğer paketleri yükle
pip install -r requirements.txt
```

#### **Intel Mac/Linux/Windows için:**
```bash
# Sanal ortamı yeniden oluştur
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 🧠 **Model Yükleme Hatası**
```bash
# Transformers cache'ini temizle
rm -rf ~/.cache/huggingface/
python3 app.py
```

## 🔒 Güvenlik

- ✅ **CORS**: Cross-origin requests aktif
- ✅ **Input Validation**: Kullanıcı girdisi doğrulanır
- ✅ **Error Handling**: Hata yönetimi mevcut
- ✅ **Rate Limiting**: İstek sınırlaması (gelecek sürümde)

## 📈 Performans

### ⚡ **Optimizasyonlar**
- 🚀 **Model Caching**: Modeller bellekte tutulur
- ⚡ **Response Caching**: Yanıtlar önbelleğe alınır
- 🎯 **Prompt Optimization**: Gelişmiş prompt mühendisliği
- 📱 **Mobile Optimization**: Mobil cihazlar için optimize

### 📊 **Benchmark**
- **Yanıt Süresi**: ~2-5 saniye
- **Model Yükleme**: ~30-60 saniye (ilk açılışta)
- **Bellek Kullanımı**: ~2-4GB RAM
- **CPU Kullanımı**: %20-40 (ortalama)

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 👨‍💻 Geliştirici

**Tahsin AI** - Turkish GPT-2 Destekli Akıllı Asistan

## 🙏 Teşekkürler

- 🤗 **Hugging Face**: Transformers kütüphanesi
- 🏫 **YTU-CE-Cosmos**: Turkish GPT-2 modeli
- 🏢 **Microsoft**: DialoGPT-medium modeli
- 🏢 **Google**: Flan-T5-base modeli
- 🎨 **CSS Animations**: Modern animasyonlar

---

⭐ **Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!** ⭐ 