import pandas as pd

import matplotlib.pyplot as plt
# Step 1: Load CSV file
df = pd.read_csv("temperature_log.csv")

# Step 2: Convert 'reading' column to numeric, coercing invalid entries to NaN
df['reading'] = pd.to_numeric(df['reading'], errors='coerce')

# Step 3: Drop rows with NaN (invalid readings)
clean_df = df.dropna(subset=['reading'])

# Step 4: Compute summary stats
min_temp = clean_df['reading'].min()
max_temp = clean_df['reading'].max()
avg_temp = clean_df['reading'].mean()
range_temp = max_temp - min_temp

# Step 5: Most common temperature
most_common_temp = clean_df['reading'].mode()[0]

print("\n===== Pandas Temperature Summary =====")
print(f"Total valid readings: {len(clean_df)}")
print(f"Min: {min_temp}°C | Max: {max_temp}°C | Avg: {avg_temp:.2f}°C")
print(f"Range: {range_temp}°C | Most Common: {most_common_temp}°C")
print("Stable 🌤️" if range_temp < 10 else "High Variation 🌡️")

# Step 6: (Optional) Quick visualization
clean_df['reading'].hist(bins=10, edgecolor='black', figsize=(7,5), grid=False)
plt.title("Temperature Distribution")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.grid(alpha=0.3)
plt.show()