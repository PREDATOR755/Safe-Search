import pandas as pd
import numpy as np

# Create a "Big Tech" style dataset
data = {
    'Date': pd.date_range(start='2025-01-01', periods=100),
    'Product': np.random.choice(['AI Server', 'Quantum Chip', 'VR Headset', 'Cloud Subscription'], 100),
    'Region': np.random.choice(['North America', 'Europe', 'Asia Pacific'], 100),
    'Sales': np.random.randint(5000, 50000, 100), # Random sales numbers
    'Profit_Margin': np.random.uniform(10, 45, 100) # Random margins
}

df = pd.DataFrame(data)

# Add some "trends" for the AI to find
# (e.g., Make AI Servers very expensive)
df.loc[df['Product'] == 'AI Server', 'Sales'] *= 1.5

df.to_csv("global_tech_sales.csv", index=False)
print("✅ Generated 'global_tech_sales.csv'. Ready for analysis!")