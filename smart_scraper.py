import pandas as pd
import requests
import re
from io import StringIO

class SmartiPhoneScraper:
    def __init__(self):
        self.results = []
    
    def scrape_google_sheet(self, sheet_id, gid=0):
        """Scrape a Google Sheet and return data"""
        try:
            url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
            response = requests.get(url)
            
            if response.status_code == 200:
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
        print("Extracting data from VELTRON...")
        
        sheet_id = "198QWur8qCBD54um63W2AQxiHzBO5nO4qiv9GB_znEm8"
        df = self.scrape_google_sheet(sheet_id)
        
        if df is not None:
            for index, row in df.iterrows():
                row_text = ' '.join(str(cell) for cell in row.values if pd.notna(cell))
                
                # Look for iPhone patterns
                if 'IPHONE' in row_text.upper():
                    # Extract model and GB
                    model_match = re.search(r'(IPHONE\s+\d+(?:\s+PLUS|\s+PRO\s+MAX|\s+PRO|\s+E)?)', row_text.upper())
                    gb_match = re.search(r'(\d+(?:GB|TB))', row_text.upper())
                    price_match = re.search(r'(\d+)\s*\$', row_text)
                    
                    if model_match and gb_match and price_match:
                        modelo = model_match.group(1).strip()
                        gb = gb_match.group(1).strip()
                        precio = price_match.group(1).strip()
                        
                        # Determine condition
                        condicion = "Nuevo"
                        if "REACOND" in row_text.upper():
                            condicion = "Reacondicionado"
                        elif "USADO" in row_text.upper() or "SEMINUEVO" in row_text.upper():
                            condicion = "Usado"
                        
                        self.results.append({
                            'Pagina': 'VELTRON - LISTA DE PRECIOS',
                            'Modelo': modelo,
                            'GB': gb,
                            'Precio_USD': precio,
                            'Condicion': condicion
                        })
    
    def extract_tecnostore_data(self):
        """Extract data from TECNOSTORE sheet"""
        print("Extracting data from TECNOSTORE...")
        
        sheet_id = "1gwxYedsFCUoqiHTaFaaDQRK9a4-aASerRbdWtLHoKEU"
        df = self.scrape_google_sheet(sheet_id)
        
        if df is not None:
            for index, row in df.iterrows():
                row_text = ' '.join(str(cell) for cell in row.values if pd.notna(cell))
                
                # Look for iPhone patterns
                if 'IPHONE' in row_text.upper():
                    # Extract model and GB
                    model_match = re.search(r'(IPHONE\s+\d+(?:\s+PLUS|\s+PRO\s+MAX|\s+PRO|\s+E)?)', row_text.upper())
                    gb_match = re.search(r'(\d+(?:GB|TB))', row_text.upper())
                    price_match = re.search(r'\$(\d+)', row_text)
                    
                    if model_match and gb_match and price_match:
                        modelo = model_match.group(1).strip()
                        gb = gb_match.group(1).strip()
                        precio = price_match.group(1).strip()
                        
                        # Determine condition
                        condicion = "Nuevo"
                        if "USADO" in row_text.upper():
                            condicion = "Usado"
                        
                        self.results.append({
                            'Pagina': 'TECNOSTORE_ARG',
                            'Modelo': modelo,
                            'GB': gb,
                            'Precio_USD': precio,
                            'Condicion': condicion
                        })
    
    def extract_masstore_data(self):
        """Extract data from MasStore sheet"""
        print("Extracting data from MasStore...")
        
        sheet_id = "1X15AlC-UEJesjD8Tv3ZGF8RhwS-xmKXBqfWw5P2AZt0"
        df = self.scrape_google_sheet(sheet_id)
        
        if df is not None:
            for index, row in df.iterrows():
                row_text = ' '.join(str(cell) for cell in row.values if pd.notna(cell))
                
                # Look for iPhone patterns
                if 'IPHONE' in row_text.upper():
                    # Extract model and GB
                    model_match = re.search(r'(IPHONE\s+\d+(?:\s+PLUS|\s+PRO\s+MAX|\s+PRO|\s+E)?)', row_text.upper())
                    gb_match = re.search(r'(\d+(?:GB|TB))', row_text.upper())
                    price_match = re.search(r'\$(\d+)', row_text)
                    
                    if model_match and gb_match and price_match:
                        modelo = model_match.group(1).strip()
                        gb = gb_match.group(1).strip()
                        precio = price_match.group(1).strip()
                        
                        # Determine condition
                        condicion = "Nuevo"
                        if "USADO" in row_text.upper() or "BATERIA" in row_text.upper():
                            condicion = "Usado"
                        
                        self.results.append({
                            'Pagina': 'MasStore',
                            'Modelo': modelo,
                            'GB': gb,
                            'Precio_USD': precio,
                            'Condicion': condicion
                        })
    
    def extract_iphoneshop_data(self):
        """Extract data from iPhoneShop sheet"""
        print("Extracting data from iPhoneShop...")
        
        sheet_id = "1psDS5fzAi9csX21qif_RZ4r2eKN-ejnqvnd9lYdAuAQ"
        df = self.scrape_google_sheet(sheet_id, gid=218823156)
        
        if df is not None:
            for index, row in df.iterrows():
                row_text = ' '.join(str(cell) for cell in row.values if pd.notna(cell))
                
                # Look for iPhone patterns
                if 'IPHONE' in row_text.upper():
                    # Extract model and GB
                    model_match = re.search(r'(IPHONE\s+\d+(?:\s+PLUS|\s+PRO\s+MAX|\s+PRO|\s+E)?)', row_text.upper())
                    gb_match = re.search(r'(\d+(?:GB|TB))', row_text.upper())
                    price_match = re.search(r'(\d+)\s*\$', row_text)
                    
                    if model_match and gb_match and price_match:
                        modelo = model_match.group(1).strip()
                        gb = gb_match.group(1).strip()
                        precio = price_match.group(1).strip()
                        
                        # Determine condition
                        condicion = "Nuevo"
                        if "USADO" in row_text.upper():
                            condicion = "Usado"
                        
                        self.results.append({
                            'Pagina': 'iPhoneShop',
                            'Modelo': modelo,
                            'GB': gb,
                            'Precio_USD': precio,
                            'Condicion': condicion
                        })
    
    def scrape_all_sheets(self):
        """Scrape all sheets and return results"""
        print("🚀 Starting SMART data extraction...")
        
        self.extract_veltron_data()
        self.extract_tecnostore_data()
        self.extract_masstore_data()
        self.extract_iphoneshop_data()
        
        print(f"✅ Extracted {len(self.results)} SMART products")
        return self.results

def main():
    scraper = SmartiPhoneScraper()
    results = scraper.scrape_all_sheets()
    
    if results:
        # Create DataFrame and save to CSV
        df = pd.DataFrame(results)
        df.to_csv('iphone_prices_smart.csv', index=False)
        print(f"💾 Saved {len(results)} SMART products to iphone_prices_smart.csv")
        
        # Show summary
        print("\n📊 Summary:")
        for store in df['Pagina'].unique():
            count = len(df[df['Pagina'] == store])
            print(f"  {store}: {count} products")
        
        # Show sample data
        print("\n📱 Sample data:")
        print(df.head(10).to_string())
    else:
        print("❌ No data extracted")

if __name__ == "__main__":
    main() 