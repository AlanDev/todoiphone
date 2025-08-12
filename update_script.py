#!/usr/bin/env python3
"""
Script para actualizar datos de iPhone automáticamente
"""

import subprocess
import time
import schedule
from datetime import datetime

def update_data():
    """Ejecuta el scraper y actualiza los datos"""
    try:
        print(f"[{datetime.now()}] Actualizando datos...")
        
        # Ejecutar el scraper
        result = subprocess.run(['python', 'simple_scraper.py'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"[{datetime.now()}] ✅ Datos actualizados correctamente")
        else:
            print(f"[{datetime.now()}] ❌ Error al actualizar: {result.stderr}")
            
    except Exception as e:
        print(f"[{datetime.now()}] ❌ Error: {e}")

def main():
    """Función principal"""
    print("🤖 Iniciando actualizador automático de datos...")
    print("📅 Los datos se actualizarán cada 6 horas")
    
    # Programar actualización cada 6 horas
    schedule.every(6).hours.do(update_data)
    
    # Ejecutar una vez al inicio
    update_data()
    
    # Mantener el script corriendo
    while True:
        schedule.run_pending()
        time.sleep(60)  # Verificar cada minuto

if __name__ == "__main__":
    main() 