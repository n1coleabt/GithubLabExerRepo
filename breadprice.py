import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('breadprice.csv')
df = df.dropna()
df

# Calculate the average price for each year
df['Average Price'] = df.mean(axis=1)  # Calculate mean along rows
# Extract year and average price columns
year_price_df = df[['Year', 'Average Price']]
df

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(year_price_df['Year'], year_price_df['Average Price'], marker='o')
plt.title('Average Price of Bread Each Year')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.grid(True)
plt.xticks(year_price_df['Year'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
