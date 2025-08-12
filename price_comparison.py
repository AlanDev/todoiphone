import pandas as pd
from simple_scraper import SimpleiPhoneScraper

class PriceComparison:
    def __init__(self):
        self.scraper = SimpleiPhoneScraper()
        self.df = None
    
    def load_data(self):
        """Load data from the scraper"""
        print("Loading iPhone price data...")
        self.scraper.scrape_all_sheets()
        
        if self.scraper.results:
            self.df = pd.DataFrame(self.scraper.results)
            self.df['Precio_USD'] = pd.to_numeric(self.df['Precio_USD'])
            print(f"Loaded {len(self.df)} iPhone records")
        else:
            print("No data available")
    
    def compare_prices_by_model(self):
        """Compare prices for the same models between stores"""
        print("\n" + "=" * 80)
        print("PRICE COMPARISON BY MODEL")
        print("=" * 80)
        
        if self.df is None:
            print("No data available for comparison")
            return
        
        # Group by model and GB to find matching products
        comparison_data = []
        
        for (model, gb), group in self.df.groupby(['Modelo', 'GB']):
            if len(group) > 1:  # Multiple stores have this model
                stores = group['Pagina'].tolist()
                prices = group['Precio_USD'].tolist()
                conditions = group['Condicion'].tolist()
                
                # Find the best price
                min_price = min(prices)
                min_price_store = stores[prices.index(min_price)]
                
                # Find the highest price
                max_price = max(prices)
                max_price_store = stores[prices.index(max_price)]
                
                price_diff = max_price - min_price
                price_diff_percent = (price_diff / min_price) * 100
                
                comparison_data.append({
                    'Modelo': model,
                    'GB': gb,
                    'Stores': len(group),
                    'Min_Price': min_price,
                    'Min_Store': min_price_store,
                    'Max_Price': max_price,
                    'Max_Store': max_price_store,
                    'Price_Diff': price_diff,
                    'Price_Diff_Percent': price_diff_percent,
                    'Conditions': ', '.join(set(conditions))
                })
        
        if comparison_data:
            comparison_df = pd.DataFrame(comparison_data)
            comparison_df = comparison_df.sort_values('Price_Diff_Percent', ascending=False)
            
            print(f"{'Modelo':<15} {'GB':<8} {'Min Price':<10} {'Max Price':<10} {'Diff':<8} {'% Diff':<8} {'Best Store':<20}")
            print("-" * 90)
            
            for _, row in comparison_df.iterrows():
                print(f"{row['Modelo']:<15} {row['GB']:<8} ${row['Min_Price']:<9} ${row['Max_Price']:<9} ${row['Price_Diff']:<7} {row['Price_Diff_Percent']:.1f}%{'':<6} {row['Min_Store']:<20}")
            
            # Save comparison to CSV
            comparison_df.to_csv('price_comparison.csv', index=False, encoding='utf-8-sig')
            print(f"\nDetailed comparison saved to 'price_comparison.csv'")
            
        else:
            print("No matching models found between stores")
    
    def store_analysis(self):
        """Analyze each store's pricing strategy"""
        print("\n" + "=" * 80)
        print("STORE ANALYSIS")
        print("=" * 80)
        
        if self.df is None:
            print("No data available for analysis")
            return
        
        for store in self.df['Pagina'].unique():
            store_data = self.df[self.df['Pagina'] == store]
            
            print(f"\n{store}:")
            print(f"  Total iPhones: {len(store_data)}")
            print(f"  Price Range: ${store_data['Precio_USD'].min()} - ${store_data['Precio_USD'].max()}")
            print(f"  Average Price: ${store_data['Precio_USD'].mean():.2f}")
            print(f"  Median Price: ${store_data['Precio_USD'].median():.2f}")
            
            # Condition breakdown
            condition_counts = store_data['Condicion'].value_counts()
            print("  By Condition:")
            for condition, count in condition_counts.items():
                print(f"    {condition}: {count} items")
    
    def best_deals(self):
        """Find the best deals by condition"""
        print("\n" + "=" * 80)
        print("BEST DEALS BY CONDITION")
        print("=" * 80)
        
        if self.df is None:
            print("No data available for analysis")
            return
        
        for condition in self.df['Condicion'].unique():
            condition_data = self.df[self.df['Condicion'] == condition]
            
            print(f"\n{condition.upper()} iPhones:")
            
            # Find best deals (lowest prices)
            best_deals = condition_data.nsmallest(5, 'Precio_USD')
            
            print(f"{'Modelo':<15} {'GB':<8} {'Precio':<10} {'Tienda':<25}")
            print("-" * 60)
            
            for _, deal in best_deals.iterrows():
                print(f"{deal['Modelo']:<15} {deal['GB']:<8} ${deal['Precio_USD']:<9} {deal['Pagina']:<25}")
    
    def price_distribution(self):
        """Show price distribution analysis"""
        print("\n" + "=" * 80)
        print("PRICE DISTRIBUTION ANALYSIS")
        print("=" * 80)
        
        if self.df is None:
            print("No data available for analysis")
            return
        
        # Price ranges
        price_ranges = [
            (0, 500, "Under $500"),
            (500, 800, "$500-$800"),
            (800, 1200, "$800-$1200"),
            (1200, 2000, "$1200-$2000"),
            (2000, float('inf'), "Over $2000")
        ]
        
        print("Price Distribution:")
        for min_price, max_price, label in price_ranges:
            if max_price == float('inf'):
                count = len(self.df[self.df['Precio_USD'] >= min_price])
            else:
                count = len(self.df[(self.df['Precio_USD'] >= min_price) & (self.df['Precio_USD'] < max_price)])
            
            percentage = (count / len(self.df)) * 100
            print(f"  {label}: {count} items ({percentage:.1f}%)")
        
        # By model series
        print("\nBy iPhone Series:")
        self.df['Series'] = self.df['Modelo'].str.extract(r'IPHONE (\d+)')[0]
        series_counts = self.df['Series'].value_counts().sort_index()
        
        for series, count in series_counts.items():
            avg_price = self.df[self.df['Series'] == series]['Precio_USD'].mean()
            print(f"  iPhone {series}: {count} items, avg price: ${avg_price:.0f}")
    
    def generate_report(self):
        """Generate a comprehensive price analysis report"""
        print("Generating comprehensive price analysis report...")
        
        self.load_data()
        self.compare_prices_by_model()
        self.store_analysis()
        self.best_deals()
        self.price_distribution()
        
        # Save summary to file
        with open('price_analysis_report.txt', 'w', encoding='utf-8') as f:
            f.write("IPHONE PRICE ANALYSIS REPORT\n")
            f.write("=" * 50 + "\n\n")
            
            if self.df is not None:
                f.write(f"Total iPhones analyzed: {len(self.df)}\n")
                f.write(f"Stores analyzed: {', '.join(self.df['Pagina'].unique())}\n")
                f.write(f"Price range: ${self.df['Precio_USD'].min()} - ${self.df['Precio_USD'].max()}\n")
                f.write(f"Average price: ${self.df['Precio_USD'].mean():.2f}\n\n")
                
                f.write("RECOMMENDATIONS:\n")
                f.write("-" * 20 + "\n")
                
                # Find best overall deals
                best_deals = self.df.nsmallest(3, 'Precio_USD')
                f.write("Best overall deals:\n")
                for _, deal in best_deals.iterrows():
                    f.write(f"  {deal['Modelo']} {deal['GB']} - ${deal['Precio_USD']} at {deal['Pagina']} ({deal['Condicion']})\n")
                
                f.write("\nBest deals by condition:\n")
                for condition in self.df['Condicion'].unique():
                    condition_data = self.df[self.df['Condicion'] == condition]
                    best = condition_data.loc[condition_data['Precio_USD'].idxmin()]
                    f.write(f"  {condition}: {best['Modelo']} {best['GB']} - ${best['Precio_USD']} at {best['Pagina']}\n")
        
        print("\nReport saved to 'price_analysis_report.txt'")

def main():
    analyzer = PriceComparison()
    analyzer.generate_report()

if __name__ == "__main__":
    main() 