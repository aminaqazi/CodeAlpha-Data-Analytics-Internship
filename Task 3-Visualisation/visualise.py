import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\amina_98geew2\OneDrive\Documents\CodeAlpha Internship\Task 1-Web Scraping\Zameen.pk\Task 2-EDA\CodeAlpha_Task2_Cleaned.csv")
valid_prices = df[df['Price_Numeric'] > 0]

sns.set_theme(style="whitegrid")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Top 10 Locations
top_10 = df['Location'].value_counts().head(10)
sns.barplot(x=top_10.values, y=top_10.index, ax=ax1, palette="viridis", hue=top_10.index, legend=False)
ax1.set_title("Market Volume by Location", fontsize=14, fontweight='bold')

# Plot 2: Price Density (Crores)
prices_in_crore = valid_prices['Price_Numeric'] / 10000000
sns.kdeplot(prices_in_crore, fill=True, color="skyblue", ax=ax2)
ax2.set_title("Price Distribution Density", fontsize=14, fontweight='bold')
ax2.set_xlabel("Price in Crore PKR")

plt.tight_layout()
plt.savefig("Lahore_Market_Analysis.png")
plt.show()