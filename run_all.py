#!/usr/bin/env python3
"""
iPhone Price Scraper - Complete Solution
========================================

This script runs all the scrapers and analysis tools to provide a complete
iPhone price comparison solution.

Files created:
- iphone_prices.csv: Raw data from both stores
- iphone_prices_live.csv: Live data (if available)
- price_comparison.csv: Detailed price comparison
- price_analysis_report.txt: Comprehensive analysis report
"""

import os
import sys
from datetime import datetime

def print_header():
    """Print a nice header"""
    print("=" * 80)
    print("📱 IPHONE PRICE SCRAPER - COMPLETE SOLUTION")
    print("=" * 80)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

def print_section(title):
    """Print a section header"""
    print(f"\n{'='*60}")
    print(f"🔍 {title}")
    print(f"{'='*60}")

def main():
    """Run all scrapers and analysis tools"""
    print_header()
    
    # Step 1: Run simple scraper
    print_section("STEP 1: EXTRACTING DATA FROM GOOGLE SHEETS")
    try:
        print("Running simple scraper...")
        from simple_scraper import SimpleiPhoneScraper
        scraper = SimpleiPhoneScraper()
        scraper.scrape_all_sheets()
        scraper.save_results('iphone_prices.csv')
        print("✅ Simple scraper completed successfully")
    except Exception as e:
        print(f"❌ Error in simple scraper: {e}")
    
    # Step 2: Run live scraper (optional)
    print_section("STEP 2: ATTEMPTING LIVE DATA EXTRACTION")
    try:
        print("Running live scraper...")
        from live_scraper import LiveiPhoneScraper
        live_scraper = LiveiPhoneScraper()
        live_scraper.scrape_all_sheets()
        live_scraper.save_results('iphone_prices_live.csv')
        print("✅ Live scraper completed successfully")
    except Exception as e:
        print(f"⚠️  Live scraper had issues (using fallback data): {e}")
    
    # Step 3: Run price comparison analysis
    print_section("STEP 3: GENERATING PRICE ANALYSIS")
    try:
        print("Running price comparison analysis...")
        from price_comparison import PriceComparison
        analyzer = PriceComparison()
        analyzer.generate_report()
        print("✅ Price analysis completed successfully")
    except Exception as e:
        print(f"❌ Error in price analysis: {e}")
    
    # Step 4: Show summary of created files
    print_section("STEP 4: SUMMARY OF CREATED FILES")
    
    files_created = []
    expected_files = [
        'iphone_prices.csv',
        'iphone_prices_live.csv', 
        'price_comparison.csv',
        'price_analysis_report.txt'
    ]
    
    for file in expected_files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            files_created.append((file, size))
            print(f"✅ {file} ({size} bytes)")
        else:
            print(f"❌ {file} (not created)")
    
    # Step 5: Show quick summary
    print_section("STEP 5: QUICK SUMMARY")
    
    if os.path.exists('iphone_prices.csv'):
        import pandas as pd
        df = pd.read_csv('iphone_prices.csv')
        print(f"📊 Total iPhones analyzed: {len(df)}")
        print(f"🏪 Stores analyzed: {', '.join(df['Pagina'].unique())}")
        print(f"💰 Price range: ${df['Precio_USD'].min()} - ${df['Precio_USD'].max()}")
        print(f"📈 Average price: ${df['Precio_USD'].mean():.2f}")
        
        # Best deals
        best_deals = df.nsmallest(3, 'Precio_USD')
        print(f"\n🏆 Top 3 Best Deals:")
        for _, deal in best_deals.iterrows():
            print(f"   {deal['Modelo']} {deal['GB']} - ${deal['Precio_USD']} at {deal['Pagina']} ({deal['Condicion']})")
    
    print_section("COMPLETED")
    print("🎉 All scraping and analysis tasks completed!")
    print(f"Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n📁 Check the generated files for detailed results:")
    for file, size in files_created:
        print(f"   • {file}")

if __name__ == "__main__":
    main() 