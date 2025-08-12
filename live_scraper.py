import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import json
from io import StringIO

class LiveiPhoneScraper:
    def __init__(self):
        self.results = []
    
    def scrape_google_sheet(self, sheet_id, gid=0):
        """Scrape a Google Sheet and return data"""
        try:
            # Convert to CSV format
            url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
            response = requests.get(url)
            
            if response.status_code == 200:
                # Read CSV data
                df = pd.read_csv(StringIO(response.text))
                return df
            else:
                print(f"❌ Error accessing sheet: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Error scraping sheet: {e}")
            return None
    
    def extract_veltron_data(self):
        """Extract data from VELTRON sheet"""
        print("Extracting LIVE data from VELTRON...")
        
        # VELTRON sheet ID
        sheet_id = "198QWur8qCBD54um63W2AQxiHzBO5nO4qiv9GB_znEm8"
        
        df = self.scrape_google_sheet(sheet_id)
        if df is not None:
            print(f"✅ Found {len(df)} rows in VELTRON sheet")
            
            # Process each row
            for index, row in df.iterrows():
                try:
                    # Extract data from columns (adjust column names as needed)
                    modelo = str(row.get('Modelo', row.get('MODELO', ''))).strip()
                    gb = str(row.get('GB', row.get('Capacidad', ''))).strip()
                    precio = str(row.get('Precio USD', row.get('Precio_USD', row.get('Precio', '')))).strip()
                    condicion = str(row.get('Condición', row.get('Condicion', row.get('Estado', '')))).strip()
                    
                    # Clean and validate data
                    if modelo and gb and precio and condicion:
                        # Remove currency symbols and clean price
                        precio = re.sub(r'[^\d.]', '', precio)
                        
                        if precio and float(precio) > 0:
                            self.results.append({
                                'Pagina': 'VELTRON - LISTA DE PRECIOS',
                                'Modelo': modelo.upper(),
                                'GB': gb.upper(),
                                'Precio_USD': precio,
                                'Condicion': condicion.title()
                            })
                            
                except Exception as e:
                    print(f"⚠️ Error processing row {index}: {e}")
                    continue
        else:
            print("❌ Could not access VELTRON sheet")
    
    def extract_tecnostore_data(self):
        """Extract data from TECNOSTORE sheet"""
        print("Extracting LIVE data from TECNOSTORE...")
        
        # TECNOSTORE sheet ID
        sheet_id = "1gwxYedsFCUoqiHTaFaaDQRK9a4-aASerRbdWtLHoKEU"
        
        df = self.scrape_google_sheet(sheet_id)
        if df is not None:
            print(f"✅ Found {len(df)} rows in TECNOSTORE sheet")
            
            # Process each row
            for index, row in df.iterrows():
                try:
                    # Extract data from columns (adjust column names as needed)
                    modelo = str(row.get('Modelo', row.get('MODELO', ''))).strip()
                    gb = str(row.get('GB', row.get('Capacidad', ''))).strip()
                    precio = str(row.get('Precio USD', row.get('Precio_USD', row.get('Precio', '')))).strip()
                    condicion = str(row.get('Condición', row.get('Condicion', row.get('Estado', '')))).strip()
                    
                    # Clean and validate data
                    if modelo and gb and precio and condicion:
                        # Remove currency symbols and clean price
                        precio = re.sub(r'[^\d.]', '', precio)
                        
                        if precio and float(precio) > 0:
                            self.results.append({
                                'Pagina': 'TECNOSTORE_ARG',
                                'Modelo': modelo.upper(),
                                'GB': gb.upper(),
                                'Precio_USD': precio,
                                'Condicion': condicion.title()
                            })
                            
                except Exception as e:
                    print(f"⚠️ Error processing row {index}: {e}")
                    continue
        else:
            print("❌ Could not access TECNOSTORE sheet")
    
    def extract_masstore_data(self):
        """Extract data from MasStore sheet"""
        print("Extracting LIVE data from MasStore...")
        
        # MasStore sheet ID
        sheet_id = "1X15AlC-UEJesjD8Tv3ZGF8RhwS-xmKXBqfWw5P2AZt0"
        
        df = self.scrape_google_sheet(sheet_id)
        if df is not None:
            print(f"✅ Found {len(df)} rows in MasStore sheet")
            
            # Process each row
            for index, row in df.iterrows():
                try:
                    # Extract data from columns (adjust column names as needed)
                    modelo = str(row.get('Modelo', row.get('MODELO', ''))).strip()
                    gb = str(row.get('GB', row.get('Capacidad', ''))).strip()
                    precio = str(row.get('Precio USD', row.get('Precio_USD', row.get('Precio', '')))).strip()
                    condicion = str(row.get('Condición', row.get('Condicion', row.get('Estado', '')))).strip()
                    
                    # Clean and validate data
                    if modelo and gb and precio and condicion:
                        # Remove currency symbols and clean price
                        precio = re.sub(r'[^\d.]', '', precio)
                        
                        if precio and float(precio) > 0:
                            self.results.append({
                                'Pagina': 'MasStore',
                                'Modelo': modelo.upper(),
                                'GB': gb.upper(),
                                'Precio_USD': precio,
                                'Condicion': condicion.title()
                            })
                            
                except Exception as e:
                    print(f"⚠️ Error processing row {index}: {e}")
                    continue
        else:
            print("❌ Could not access MasStore sheet")
    
    def extract_iphoneshop_data(self):
        """Extract data from iPhoneShop sheet"""
        print("Extracting LIVE data from iPhoneShop...")
        
        # iPhoneShop sheet ID
        sheet_id = "1psDS5fzAi9csX21qif_RZ4r2eKN-ejnqvnd9lYdAuAQ"
        
        df = self.scrape_google_sheet(sheet_id, gid=218823156)
        if df is not None:
            print(f"✅ Found {len(df)} rows in iPhoneShop sheet")
            
            # Process each row
            for index, row in df.iterrows():
                try:
                    # Extract data from columns (adjust column names as needed)
                    modelo = str(row.get('Modelo', row.get('MODELO', ''))).strip()
                    gb = str(row.get('GB', row.get('Capacidad', ''))).strip()
                    precio = str(row.get('Precio USD', row.get('Precio_USD', row.get('Precio', '')))).strip()
                    condicion = str(row.get('Condición', row.get('Condicion', row.get('Estado', '')))).strip()
                    
                    # Clean and validate data
                    if modelo and gb and precio and condicion:
                        # Remove currency symbols and clean price
                        precio = re.sub(r'[^\d.]', '', precio)
                        
                        if precio and float(precio) > 0:
                            self.results.append({
                                'Pagina': 'iPhoneShop',
                                'Modelo': modelo.upper(),
                                'GB': gb.upper(),
                                'Precio_USD': precio,
                                'Condicion': condicion.title()
                            })
                            
                except Exception as e:
                    print(f"⚠️ Error processing row {index}: {e}")
                    continue
        else:
            print("❌ Could not access iPhoneShop sheet")
    
    def scrape_all_sheets(self):
        """Scrape all sheets and return results"""
        print("🚀 Starting LIVE data extraction...")
        
        self.extract_veltron_data()
        self.extract_tecnostore_data()
        self.extract_masstore_data()
        self.extract_iphoneshop_data()
        
        print(f"✅ Extracted {len(self.results)} LIVE products")
        return self.results

def main():
    scraper = LiveiPhoneScraper()
    results = scraper.scrape_all_sheets()
    
    if results:
        # Create DataFrame and save to CSV
        df = pd.DataFrame(results)
        df.to_csv('iphone_prices_live.csv', index=False)
        print(f"💾 Saved {len(results)} LIVE products to iphone_prices_live.csv")
        
        # Show summary
        print("\n📊 Summary:")
        for store in df['Pagina'].unique():
            count = len(df[df['Pagina'] == store])
            print(f"  {store}: {count} products")
    else:
        print("❌ No data extracted")

if __name__ == "__main__":
    main() 