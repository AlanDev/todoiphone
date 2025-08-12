import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import json

class SimpleiPhoneScraper:
    def __init__(self):
        self.results = []
    
    def extract_veltron_data(self):
        """Extract data from VELTRON sheet based on provided information"""
        print("Extracting data from VELTRON - LISTA DE PRECIOS...")
        
        # Data extracted from the provided sheet information
        veltron_data = [
            # New/Refurbished iPhones
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
            
            # Used iPhones - Datos reales del spreadsheet
            {"modelo": "IPHONE 11", "gb": "128 GB", "precio": "310", "condicion": "Usado"},
            {"modelo": "IPHONE 12", "gb": "64 GB", "precio": "320", "condicion": "Usado"},
            {"modelo": "IPHONE 12 PRO MAX", "gb": "256 GB", "precio": "500", "condicion": "Usado"},
            {"modelo": "IPHONE 12 PRO", "gb": "256 GB", "precio": "450", "condicion": "Usado"},
            {"modelo": "IPHONE 13", "gb": "128 GB", "precio": "500", "condicion": "Usado"},
            {"modelo": "IPHONE 13", "gb": "128 GB", "precio": "540", "condicion": "Usado"},
            {"modelo": "IPHONE 13 PRO", "gb": "128GB", "precio": "480", "condicion": "Usado"},
            {"modelo": "IPHONE 14", "gb": "128 GB", "precio": "490", "condicion": "Usado"},
            {"modelo": "IPHONE 14", "gb": "128 GB", "precio": "540", "condicion": "Usado"},
            {"modelo": "IPHONE 14", "gb": "128 GB", "precio": "570", "condicion": "Usado"},
            {"modelo": "IPHONE 14 PRO MAX", "gb": "512GB", "precio": "840", "condicion": "Usado"},
            {"modelo": "IPHONE 15", "gb": "128 GB", "precio": "640", "condicion": "Usado"},
            {"modelo": "IPHONE 15", "gb": "128 GB", "precio": "670", "condicion": "Usado"},
            {"modelo": "IPHONE 15", "gb": "128 GB", "precio": "690", "condicion": "Usado"},
            {"modelo": "IPHONE 15", "gb": "128 GB", "precio": "710", "condicion": "Usado"},
            {"modelo": "IPHONE 15 PRO", "gb": "128 GB", "precio": "860", "condicion": "Usado"},
            {"modelo": "IPHONE 15 PRO", "gb": "128 GB", "precio": "900", "condicion": "Usado"},
            {"modelo": "IPHONE 15 PRO", "gb": "256 GB", "precio": "900", "condicion": "Usado"},
            {"modelo": "IPHONE 15 PRO", "gb": "256 GB", "precio": "930", "condicion": "Usado"},
            {"modelo": "IPHONE 15 PRO", "gb": "256 GB", "precio": "950", "condicion": "Usado"},
            {"modelo": "IPHONE 15 PRO", "gb": "256 GB", "precio": "950", "condicion": "Usado"},
            {"modelo": "IPHONE 15 PRO", "gb": "256 GB", "precio": "990", "condicion": "Usado"},
            {"modelo": "IPHONE 15 PRO MAX", "gb": "256 GB", "precio": "990", "condicion": "Usado"},
            {"modelo": "IPHONE 16", "gb": "128 GB", "precio": "790", "condicion": "Usado"},
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
        """Extract data from TECNOSTORE sheet based on provided information"""
        print("Extracting data from TECNOSTORE_ARG...")
        
        # Data extracted from the provided sheet information
        tecnostore_data = [
            {"modelo": "IPHONE 13", "gb": "128 GB", "precio": "580", "condicion": "Nuevo"},
            {"modelo": "IPHONE 14", "gb": "128 GB", "precio": "680", "condicion": "Nuevo"},
            {"modelo": "IPHONE 15", "gb": "128 GB", "precio": "760", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 E", "gb": "256 GB", "precio": "770", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16", "gb": "128 GB", "precio": "840", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO", "gb": "128 GB", "precio": "1060", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO", "gb": "256 GB", "precio": "1160", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO MAX", "gb": "256 GB", "precio": "1240", "condicion": "Nuevo"},
            
            # Used iPhones - Datos reales del spreadsheet
            {"modelo": "IPHONE 11", "gb": "128 GB", "precio": "300", "condicion": "Usado"},
            {"modelo": "IPHONE 12", "gb": "128 GB", "precio": "400", "condicion": "Usado"},
            {"modelo": "IPHONE 12 MINI", "gb": "128 GB", "precio": "380", "condicion": "Usado"},
            {"modelo": "IPHONE 12 PRO", "gb": "256 GB", "precio": "480", "condicion": "Usado"},
            {"modelo": "IPHONE 12 PRO MAX", "gb": "256 GB", "precio": "580", "condicion": "Usado"},
            {"modelo": "IPHONE 13", "gb": "128 GB", "precio": "400", "condicion": "Usado"},
            {"modelo": "IPHONE 13", "gb": "256 GB", "precio": "600", "condicion": "Usado"},
            {"modelo": "IPHONE 13 MINI", "gb": "128 GB", "precio": "500", "condicion": "Usado"},
            {"modelo": "IPHONE 13 PRO", "gb": "128 GB", "precio": "500", "condicion": "Usado"},
            {"modelo": "IPHONE 14", "gb": "128 GB", "precio": "500", "condicion": "Usado"},
            {"modelo": "IPHONE 15", "gb": "128 GB", "precio": "570", "condicion": "Usado"},
            {"modelo": "IPHONE 15", "gb": "256 GB", "precio": "630", "condicion": "Usado"},
            {"modelo": "IPHONE 15 PRO", "gb": "128 GB", "precio": "730", "condicion": "Usado"},
            {"modelo": "IPHONE 15 PRO", "gb": "256 GB", "precio": "800", "condicion": "Usado"},
            {"modelo": "IPHONE 15 PRO", "gb": "512 GB", "precio": "930", "condicion": "Usado"},
            {"modelo": "IPHONE 15 PRO MAX", "gb": "256 GB", "precio": "950", "condicion": "Usado"},
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
        """Extract data from MasStore sheet based on provided information"""
        print("Extracting data from MasStore...")
        
        # Data extracted from the MasStore sheet information
        masstore_data = [
            # New iPhones from MasStore - Datos reales del spreadsheet
            {"modelo": "IPHONE 11", "gb": "128GB", "precio": "500", "condicion": "Nuevo"},
            {"modelo": "IPHONE 12", "gb": "128GB", "precio": "530", "condicion": "Nuevo"},
            {"modelo": "IPHONE 13", "gb": "128GB", "precio": "580", "condicion": "Nuevo"},
            {"modelo": "IPHONE 14", "gb": "128GB", "precio": "680", "condicion": "Nuevo"},
            {"modelo": "IPHONE 15", "gb": "128GB", "precio": "760", "condicion": "Nuevo"},
            {"modelo": "IPHONE 15", "gb": "256GB", "precio": "890", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16", "gb": "128GB", "precio": "850", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16", "gb": "256GB", "precio": "1040", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO", "gb": "128GB", "precio": "1060", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO", "gb": "256GB", "precio": "1160", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO", "gb": "512GB", "precio": "1470", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO MAX", "gb": "256GB", "precio": "1240", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO MAX", "gb": "512GB", "precio": "1500", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PLUS", "gb": "128GB", "precio": "980", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PLUS", "gb": "256GB", "precio": "1090", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 E", "gb": "128GB", "precio": "740", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 E", "gb": "256GB", "precio": "770", "condicion": "Nuevo"},
            
            # Used iPhones from MasStore - Datos reales del spreadsheet
            {"modelo": "IPHONE 11", "gb": "64GB", "precio": "240", "condicion": "Usado"},
            {"modelo": "IPHONE 11", "gb": "128GB", "precio": "270", "condicion": "Usado"},
            {"modelo": "IPHONE 11", "gb": "128GB", "precio": "270", "condicion": "Usado"},
            {"modelo": "IPHONE 11", "gb": "128GB", "precio": "270", "condicion": "Usado"},
            {"modelo": "IPHONE 11", "gb": "128GB", "precio": "270", "condicion": "Usado"},
            {"modelo": "IPHONE 11", "gb": "128GB", "precio": "290", "condicion": "Usado"},
            {"modelo": "IPHONE 13 PRO", "gb": "128GB", "precio": "560", "condicion": "Usado"},
            {"modelo": "IPHONE 14", "gb": "128GB", "precio": "540", "condicion": "Usado"},
            {"modelo": "IPHONE 14", "gb": "128GB", "precio": "550", "condicion": "Usado"},
            {"modelo": "IPHONE 14", "gb": "128GB", "precio": "550", "condicion": "Usado"},
            {"modelo": "IPHONE 15", "gb": "128GB", "precio": "670", "condicion": "Usado"},
            {"modelo": "IPHONE 15", "gb": "128GB", "precio": "690", "condicion": "Usado"},
            {"modelo": "IPHONE 15", "gb": "128GB", "precio": "690", "condicion": "Usado"},
            {"modelo": "IPHONE 15", "gb": "128GB", "precio": "690", "condicion": "Usado"},
            {"modelo": "IPHONE 15 PRO", "gb": "128GB", "precio": "850", "condicion": "Usado"},
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
        """Extract data from iPhoneShop sheet based on provided information"""
        print("Extracting data from iPhoneShop...")
        
        # Data extracted from the iPhoneShop sheet information
        iphoneshop_data = [
            # New iPhones from iPhoneShop - Datos reales del spreadsheet
            {"modelo": "IPHONE 13", "gb": "128GB", "precio": "580", "condicion": "Nuevo"},
            {"modelo": "IPHONE 14", "gb": "128GB", "precio": "680", "condicion": "Nuevo"},
            {"modelo": "IPHONE 15", "gb": "128GB", "precio": "780", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16", "gb": "128GB", "precio": "860", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO", "gb": "128GB", "precio": "1060", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO", "gb": "256GB", "precio": "1160", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO MAX", "gb": "256GB", "precio": "1250", "condicion": "Nuevo"},
            {"modelo": "IPHONE 16 PRO MAX", "gb": "512GB", "precio": "1550", "condicion": "Nuevo"},
            
            # Used iPhones from iPhoneShop - Datos reales del spreadsheet (3 usados reales)
            {"modelo": "IPHONE 11", "gb": "128GB", "precio": "300", "condicion": "Usado"},
            {"modelo": "IPHONE 13 PRO MAX", "gb": "256GB", "precio": "720", "condicion": "Usado"},
            {"modelo": "IPHONE 14 PRO MAX", "gb": "128GB", "precio": "780", "condicion": "Usado"},
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
        print("🚀 Starting data extraction...")
        
        self.extract_veltron_data()
        self.extract_tecnostore_data()
        self.extract_masstore_data()
        self.extract_iphoneshop_data()
        
        print(f"✅ Extracted {len(self.results)} products")
        return self.results

def main():
    scraper = SimpleiPhoneScraper()
    results = scraper.scrape_all_sheets()
    
    # Create DataFrame and save to CSV
    df = pd.DataFrame(results)
    df.to_csv('iphone_prices.csv', index=False)
    print(f"💾 Saved {len(results)} products to iphone_prices.csv")
    
    # Show summary
    print("\n📊 Summary:")
    for store in df['Pagina'].unique():
        count = len(df[df['Pagina'] == store])
        print(f"  {store}: {count} products")

if __name__ == "__main__":
    main() 