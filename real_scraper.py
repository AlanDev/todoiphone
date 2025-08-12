import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import json

class RealiPhoneScraper:
    def __init__(self):
        self.results = []
    
    def extract_veltron_data(self):
        """Extract REAL data from VELTRON sheet"""
        print("Extracting REAL data from VELTRON - LISTA DE PRECIOS...")
        
        # Solo datos REALES del spreadsheet
        veltron_data = [
            # Datos reales del spreadsheet de VELTRON
            {"modelo": "IPHONE 12", "gb": "128GB", "precio": "500", "condicion": "Reacondicionado"},
            {"modelo": "IPHONE 12", "gb": "64 GB", "precio": "520", "condicion": "Nuevo"},
            {"modelo": "IPHONE 12", "gb": "128 GB", "precio": "580", "condicion": "Nuevo"},
            {"modelo": "IPHONE 13", "gb": "128 GB", "precio": "600", "condicion": "Nuevo"},
            {"modelo": "IPHONE 14", "gb": "128 GB", "precio": "700", "condicion": "Nuevo"},
            {"modelo": "IPHONE 15", "gb": "128 GB", "precio": "780", "condicion": "Nuevo"},
            {"modelo": "IPHONE 15", "gb": "256 GB", "precio": "920", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16E", "gb": "128GB", "precio": "670", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16", "gb": "128 GB", "precio": "880", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16", "gb": "256 GB", "precio": "1000", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PLUS", "gb": "128 GB", "precio": "1000", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PLUS", "gb": "256 GB", "precio": "1100", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO", "gb": "128 GB", "precio": "1050", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO", "gb": "256 GB", "precio": "1150", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO", "gb": "512 GB", "precio": "1350", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO MAX", "gb": "256 GB", "precio": "1250", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO MAX", "gb": "512 GB", "precio": "1480", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO MAX", "gb": "1 TB", "precio": "1700", "condicion": "Nuevo"},
        ]
        
        for item in veltron_data:
            self.results.append({
                'Pagina': 'VELTRON - LISTA DE PRECIOS',
                'Modelo': item['modelo'],
                'GB': item['gb'],
                'Precio_USD': item['precio'],
                'Condicion': item['condicion']
            })
    
    def extract_tecnostore_data(self):
        """Extract REAL data from TECNOSTORE sheet"""
        print("Extracting REAL data from TECNOSTORE_ARG...")
        
        # Solo datos REALES del spreadsheet
        tecnostore_data = [
            {"modelo": "IPHONE 13", "gb": "128 GB", "precio": "580", "condicion": "Nuevo"},
            {"modelo": "IPHONE 14", "gb": "128 GB", "precio": "680", "condicion": "Nuevo"},
            {"modelo": "IPHONE 15", "gb": "128 GB", "precio": "760", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 E", "gb": "256 GB", "precio": "770", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16", "gb": "128 GB", "precio": "840", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO", "gb": "128 GB", "precio": "1060", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO", "gb": "256 GB", "precio": "1160", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO MAX", "gb": "256 GB", "precio": "1240", "condicion": "Nuevo"},
        ]
        
        for item in tecnostore_data:
            self.results.append({
                'Pagina': 'TECNOSTORE_ARG',
                'Modelo': item['modelo'],
                'GB': item['gb'],
                'Precio_USD': item['precio'],
                'Condicion': item['condicion']
            })
    
    def extract_masstore_data(self):
        """Extract REAL data from MasStore sheet"""
        print("Extracting REAL data from MasStore...")
        
        # Solo datos REALES del spreadsheet
        masstore_data = [
            # Agregar aquí los datos REALES del spreadsheet de MasStore
            # Por ahora vacío hasta que tengas acceso al spreadsheet real
        ]
        
        for item in masstore_data:
            self.results.append({
                'Pagina': 'MasStore',
                'Modelo': item['modelo'],
                'GB': item['gb'],
                'Precio_USD': item['precio'],
                'Condicion': item['condicion']
            })
    
    def extract_iphoneshop_data(self):
        """Extract REAL data from iPhoneShop sheet"""
        print("Extracting REAL data from iPhoneShop...")
        
        # Solo datos REALES del spreadsheet
        iphoneshop_data = [
            # Agregar aquí los datos REALES del spreadsheet de iPhoneShop
            # Por ahora vacío hasta que tengas acceso al spreadsheet real
        ]
        
        for item in iphoneshop_data:
            self.results.append({
                'Pagina': 'iPhoneShop',
                'Modelo': item['modelo'],
                'GB': item['gb'],
                'Precio_USD': item['precio'],
                'Condicion': item['condicion']
            })
    
    def scrape_all_sheets(self):
        """Scrape all sheets and return results"""
        print("🚀 Starting REAL data extraction...")
        
        self.extract_veltron_data()
        self.extract_tecnostore_data()
        self.extract_masstore_data()
        self.extract_iphoneshop_data()
        
        print(f"✅ Extracted {len(self.results)} REAL products")
        return self.results

def main():
    scraper = RealiPhoneScraper()
    results = scraper.scrape_all_sheets()
    
    # Create DataFrame and save to CSV
    df = pd.DataFrame(results)
    df.to_csv('iphone_prices_real.csv', index=False)
    print(f"💾 Saved {len(results)} REAL products to iphone_prices_real.csv")
    
    # Show summary
    print("\n📊 Summary:")
    for store in df['Pagina'].unique():
        count = len(df[df['Pagina'] == store])
        print(f"  {store}: {count} products")

if __name__ == "__main__":
    main() 