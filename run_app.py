#!/usr/bin/env python3
"""
Script to run the iPhone Price Scraper Streamlit app
"""

import subprocess
import sys
import os

def main():
    print("🚀 Starting iPhone Price Scraper - CEBRA")
    print("📱 Loading Streamlit app...")
    
    try:
        # Check if streamlit is installed
        import streamlit
        print("✅ Streamlit is installed")
    except ImportError:
        print("❌ Streamlit not found. Installing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # Run the streamlit app
    print("🌐 Starting web server...")
    print("📋 The app will open in your browser at: http://localhost:8501")
    print("🔄 Press Ctrl+C to stop the server")
    
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", "app_streamlit.py",
        "--server.port", "8501",
        "--server.address", "localhost"
    ])

if __name__ == "__main__":
    main()
