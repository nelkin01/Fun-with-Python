import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load and clean data
df = pd.read_csv("temperature_log.csv")
df['reading'] = pd.to_numeric(df['reading'], errors='coerce')
clean_df = df.dropna(subset=['reading'])

# Step 2: Group by sensor and compute summary stats
group_summary = clean_df.groupby('sensor_id')['reading'].agg(
    ['count', 'min', 'max', 'mean']).reset_index()

print("\n===== Average Readings per Sensor =====")
print(group_summary)

# Step 3: Visualize average reading per sensor
plt.figure(figsize=(7,5))
plt.bar(group_summary['sensor_id'], group_summary['mean'], color='skyblue', edgecolor='black')
plt.title("Average Temperature per Sensor")
plt.xlabel("Sensor ID")
plt.ylabel("Average Temperature (°C)")
plt.grid(axis='y', alpha=0.3)
plt.show()
