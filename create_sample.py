import pandas as pd
# Read just the first 200,000 rows
df = pd.read_csv('tesla_production_big_data.csv', nrows=200000)
# Save as a smaller version
df.to_csv('tesla_sample_data.csv', index=False)
print("✅ Sample created (approx 12MB). You can now upload this via browser!")