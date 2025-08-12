import pandas as pd
import requests
from io import StringIO
import re

def deep_inspect_sheet(sheet_id, sheet_name, gid=0):
    """Deep inspect a Google Sheet to find iPhone data"""
    print(f"\n🔍 Deep inspecting {sheet_name}...")
    
    try:
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
        response = requests.get(url)
        
        if response.status_code == 200:
            df = pd.read_csv(StringIO(response.text))
            print(f"✅ Found {len(df)} rows")
            
            # Search for iPhone data in all cells
            iphone_rows = []
            for index, row in df.iterrows():
                row_text = ' '.join(str(cell) for cell in row.values if pd.notna(cell))
                if 'IPHONE' in row_text.upper() or 'IPHONE' in str(row.values).upper():
                    iphone_rows.append((index, row_text))
                    print(f"📱 Row {index}: {row_text[:200]}...")
            
            if iphone_rows:
                print(f"✅ Found {len(iphone_rows)} rows with iPhone data")
            else:
                print("❌ No iPhone data found")
                
            # Show more rows to understand structure
            print(f"\n📄 Sample rows (10-20):")
            for i in range(10, min(20, len(df))):
                row_text = ' '.join(str(cell) for cell in df.iloc[i].values if pd.notna(cell))
                if row_text.strip():
                    print(f"Row {i}: {row_text[:150]}...")
                    
            return df
        else:
            print(f"❌ Error: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    print("🔍 DEEP INSPECTING GOOGLE SHEETS")
    print("=" * 50)
    
    # VELTRON
    veltron_id = "198QWur8qCBD54um63W2AQxiHzBO5nO4qiv9GB_znEm8"
    deep_inspect_sheet(veltron_id, "VELTRON")
    
    # TECNOSTORE
    tecnostore_id = "1gwxYedsFCUoqiHTaFaaDQRK9a4-aASerRbdWtLHoKEU"
    deep_inspect_sheet(tecnostore_id, "TECNOSTORE")
    
    # MasStore
    masstore_id = "1X15AlC-UEJesjD8Tv3ZGF8RhwS-xmKXBqfWw5P2AZt0"
    deep_inspect_sheet(masstore_id, "MasStore")
    
    # iPhoneShop
    iphoneshop_id = "1psDS5fzAi9csX21qif_RZ4r2eKN-ejnqvnd9lYdAuAQ"
    deep_inspect_sheet(iphoneshop_id, "iPhoneShop", gid=218823156)

if __name__ == "__main__":
    main() 