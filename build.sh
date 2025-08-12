#!/bin/bash

echo "🚀 Starting Vercel build..."

# Instalar dependencias de Python
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Ejecutar el scraper para generar datos iniciales
echo "🔄 Running scraper to generate initial data..."
python simple_scraper.py

echo "✅ Build completed successfully!" 