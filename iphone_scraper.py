import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import json

class iPhoneScraper:
    def __init__(self):
        self.results = []
        
    def setup_driver(self):
        """Setup Chrome driver with headless options"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    
    def extract_iphone_data_veltron(self, driver):
        """Extract iPhone data from VELTRON sheet"""
        print("Extracting data from VELTRON sheet...")
        
        url = "https://docs.google.com/spreadsheets/d/198QWur8qCBD54um63W2AQxiHzBO5nO4qiv9GB_znEm8/edit?gid=0#gid=0"
        driver.get(url)
        
        # Wait for the page to load
        time.sleep(5)
        
        try:
            # Wait for the sheet to be visible
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-sheet-id]"))
            )
            
            # Get the page source after JavaScript has loaded
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            
            # Extract page name
            page_name = "VELTRON - LISTA DE PRECIOS"
            
            # Find all table rows
            rows = soup.find_all('tr')
            
            # Process new/refurbished iPhones (rows 18-36)
            for i, row in enumerate(rows[17:36]):  # Skip header, start from row 18
                cells = row.find_all(['td', 'th'])
                if len(cells) >= 2:
                    model_cell = cells[0].get_text(strip=True)
                    price_cell = cells[1].get_text(strip=True)
                    
                    # Extract iPhone data
                    if 'IPHONE' in model_cell.upper() and price_cell.replace('$', '').replace(',', '').isdigit():
                        # Extract model and GB
                        model_match = re.search(r'(IPHONE\s+\d+(?:\s+PLUS|\s+PRO\s+MAX|\s+PRO|\s+E)?)\s*(\d+(?:GB|TB))', model_cell.upper())
                        if model_match:
                            model = model_match.group(1).strip()
                            gb = model_match.group(2).strip()
                            price_usd = price_cell.replace('$', '').replace(',', '')
                            
                            # Determine if it's new or used
                            condition = "Nuevo"
                            if "REACOND" in model_cell.upper():
                                condition = "Reacondicionado"
                            
                            self.results.append({
                                'Pagina': page_name,
                                'Modelo': model,
                                'GB': gb,
                                'Precio_USD': price_usd,
                                'Condicion': condition
                            })
            
            # Process used iPhones (rows 38+)
            for i, row in enumerate(rows[37:]):  # Start from row 38
                cells = row.find_all(['td', 'th'])
                if len(cells) >= 2:
                    model_cell = cells[0].get_text(strip=True)
                    price_cell = cells[2].get_text(strip=True) if len(cells) > 2 else cells[1].get_text(strip=True)
                    
                    # Extract iPhone data
                    if 'IPHONE' in model_cell.upper() and price_cell.replace('$', '').replace(',', '').isdigit():
                        # Extract model and GB
                        model_match = re.search(r'(IPHONE\s+\d+(?:\s+PLUS|\s+PRO\s+MAX|\s+PRO|\s+E)?)\s*(\d+(?:GB|TB))', model_cell.upper())
                        if model_match:
                            model = model_match.group(1).strip()
                            gb = model_match.group(2).strip()
                            price_usd = price_cell.replace('$', '').replace(',', '')
                            
                            self.results.append({
                                'Pagina': page_name,
                                'Modelo': model,
                                'GB': gb,
                                'Precio_USD': price_usd,
                                'Condicion': "Usado"
                            })
                            
        except Exception as e:
            print(f"Error extracting data from VELTRON: {e}")
    
    def extract_iphone_data_tecnostore(self, driver):
        """Extract iPhone data from TECNOSTORE sheet"""
        print("Extracting data from TECNOSTORE sheet...")
        
        url = "https://docs.google.com/spreadsheets/u/0/d/1gwxYedsFCUoqiHTaFaaDQRK9a4-aASerRbdWtLHoKEU/htmlview"
        driver.get(url)
        
        # Wait for the page to load
        time.sleep(5)
        
        try:
            # Wait for the sheet to be visible
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
            )
            
            # Get the page source after JavaScript has loaded
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            
            # Extract page name
            page_name = "TECNOSTORE_ARG"
            
            # Find all tables
            tables = soup.find_all('table')
            
            for table in tables:
                rows = table.find_all('tr')
                
                for row in rows:
                    cells = row.find_all(['td', 'th'])
                    if len(cells) >= 3:
                        model_cell = cells[0].get_text(strip=True)
                        gb_cell = cells[1].get_text(strip=True) if len(cells) > 1 else ""
                        price_cell = cells[3].get_text(strip=True) if len(cells) > 3 else cells[2].get_text(strip=True)
                        
                        # Extract iPhone data
                        if 'IPHONE' in model_cell.upper():
                            # Extract model
                            model_match = re.search(r'(IPHONE\s+\d+(?:\s+PLUS|\s+PRO\s+MAX|\s+PRO|\s+E)?)', model_cell.upper())
                            if model_match:
                                model = model_match.group(1).strip()
                                
                                # Extract GB from GB cell or model cell
                                gb = gb_cell.strip() if gb_cell and re.search(r'\d+(?:GB|TB)', gb_cell.upper()) else ""
                                if not gb:
                                    gb_match = re.search(r'(\d+(?:GB|TB))', model_cell.upper())
                                    if gb_match:
                                        gb = gb_match.group(1).strip()
                                
                                # Extract price
                                price_match = re.search(r'(\d+)', price_cell.replace('$', '').replace(',', ''))
                                if price_match:
                                    price_usd = price_match.group(1)
                                    
                                    # Determine condition based on section
                                    condition = "Nuevo"
                                    if "USADOS" in str(table).upper() or "SEMINUEVOS" in str(table).upper():
                                        condition = "Usado"
                                    
                                    self.results.append({
                                        'Pagina': page_name,
                                        'Modelo': model,
                                        'GB': gb,
                                        'Precio_USD': price_usd,
                                        'Condicion': condition
                                    })
                                    
        except Exception as e:
            print(f"Error extracting data from TECNOSTORE: {e}")
    
    def scrape_all_sheets(self):
        """Scrape data from both Google Sheets"""
        driver = self.setup_driver()
        
        try:
            # Scrape VELTRON sheet
            self.extract_iphone_data_veltron(driver)
            
            # Scrape TECNOSTORE sheet
            self.extract_iphone_data_tecnostore(driver)
            
        finally:
            driver.quit()
    
    def save_results(self, filename='iphone_prices.csv'):
        """Save results to CSV file"""
        if self.results:
            df = pd.DataFrame(self.results)
            df.to_csv(filename, index=False, encoding='utf-8-sig')
            print(f"Results saved to {filename}")
            
            # Display results
            print("\nExtracted iPhone Data:")
            print("=" * 80)
            print(f"{'Página':<20} {'Modelo':<15} {'GB':<8} {'Precio USD':<12} {'Condición':<12}")
            print("-" * 80)
            
            for result in self.results:
                print(f"{result['Pagina']:<20} {result['Modelo']:<15} {result['GB']:<8} {result['Precio_USD']:<12} {result['Condicion']:<12}")
        else:
            print("No data extracted")

def main():
    scraper = iPhoneScraper()
    print("Starting iPhone price scraper...")
    scraper.scrape_all_sheets()
    scraper.save_results()

if __name__ == "__main__":
    main() 