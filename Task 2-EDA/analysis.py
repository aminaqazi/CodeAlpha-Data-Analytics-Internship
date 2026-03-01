import pandas as pd

df = pd.read_csv(r"C:\Users\amina_98geew2\OneDrive\Documents\CodeAlpha Internship\Task 1-Web Scraping\Zameen.pk\Task 2-EDA\CodeAlpha_Task2_Cleaned.csv")
valid_prices = df[df['Price_Numeric'] > 0]

# Calculate Statistics
avg_price = valid_prices['Price_Numeric'].mean()
median_price = valid_prices['Price_Numeric'].median() # Added Median
max_price = valid_prices['Price_Numeric'].max()

# Expanded to Top 10 Locations
location_counts = df['Location'].value_counts().head(10)

print("--- 📊 LAHORE REAL ESTATE INSIGHTS ---")
print(f"Total Listings Scraped: {len(df)}")
print(f"Average House Price: PKR {avg_price:,.0f}")
print(f"Median House Price:  PKR {median_price:,.0f}") # New Insight
print(f"Most Expensive:      PKR {max_price:,.0f}")
print("\n--- 📍 TOP 10 MARKET LOCATIONS ---")
print(location_counts)