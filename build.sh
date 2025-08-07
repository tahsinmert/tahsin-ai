#!/bin/bash

# Tahsin AI - Render Build Script
# Bu script Render platformunda deployment sırasında çalışır

echo "🚀 Tahsin AI - Render Build Script başlatılıyor..."

# Python sürümünü kontrol et
python3 --version

# Pip'i güncelle
pip install --upgrade pip

# PyTorch'u CPU versiyonu olarak yükle (Render için optimize)
echo "📦 PyTorch CPU versiyonu yükleniyor..."
pip install torch==2.8.0 torchvision==0.23.0 torchaudio==2.8.0 --index-url https://download.pytorch.org/whl/cpu

# Diğer paketleri yükle
echo "📦 Diğer paketler yükleniyor..."
pip install -r requirements.txt

# Hugging Face cache'ini temizle (opsiyonel)
echo "🧹 Cache temizleniyor..."
rm -rf ~/.cache/huggingface/

echo "✅ Build tamamlandı!"
echo "🎯 Backend başlatılıyor..." 