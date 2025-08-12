import pandas as pd
import requests
from io import StringIO

def inspect_sheet(sheet_id, sheet_name, gid=0):
    """Inspect the structure of a Google Sheet"""
    print(f"\n🔍 Inspecting {sheet_name}...")
    
    try:
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
        response = requests.get(url)
        
        if response.status_code == 200:
            df = pd.read_csv(StringIO(response.text))
            print(f"✅ Found {len(df)} rows")
            print(f"📋 Columns: {list(df.columns)}")
            print(f"📄 First 3 rows:")
            print(df.head(3).to_string())
            return df
        else:
            print(f"❌ Error: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    print("🔍 INSPECTING GOOGLE SHEETS STRUCTURE")
    print("=" * 50)
    
    # VELTRON
    veltron_id = "198QWur8qCBD54um63W2AQxiHzBO5nO4qiv9GB_znEm8"
    inspect_sheet(veltron_id, "VELTRON")
    
    # TECNOSTORE
    tecnostore_id = "1gwxYedsFCUoqiHTaFaaDQRK9a4-aASerRbdWtLHoKEU"
    inspect_sheet(tecnostore_id, "TECNOSTORE")
    
    # MasStore
    masstore_id = "1X15AlC-UEJesjD8Tv3ZGF8RhwS-xmKXBqfWw5P2AZt0"
    inspect_sheet(masstore_id, "MasStore")
    
    # iPhoneShop
    iphoneshop_id = "1psDS5fzAi9csX21qif_RZ4r2eKN-ejnqvnd9lYdAuAQ"
    inspect_sheet(iphoneshop_id, "iPhoneShop", gid=218823156)

if __name__ == "__main__":
    main() 