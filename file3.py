from collections import Counter
import matplotlib.pyplot as plt


def summarize_sensor_data(*sensors):
    # --- Step 1: Combine all readings ---
    all_temps = []
    for sensor in sensors:
        all_temps.extend(sensor)

    # --- Step 2: Clean data ---
    clean_temps = [t for t in all_temps if isinstance(t, (int, float))]
    invalid_count = len(all_temps) - len(clean_temps)

    # --- Step 3: Sort and compute statistics ---
    sorted_temps = sorted(clean_temps)
    min_temp = min(sorted_temps)
    max_temp = max(sorted_temps)
    avg_temp = sum(sorted_temps) / len(sorted_temps)

    freq_counter = Counter(sorted_temps)
    most_common_temp, count = freq_counter.most_common(1)[0]

    # --- Step 4: Print summary report ---
    print("\n===== Temperature Data Summary =====")
    print(f"Total readings received: {len(all_temps)}")
    print(f"Valid readings: {len(clean_temps)}")
    print(f"Invalid/missing readings: {invalid_count}")
    print("------------------------------------")
    print(f"Minimum temperature: {min_temp}°C")
    print(f"Maximum temperature: {max_temp}°C")
    print(f"Average temperature: {avg_temp:.2f}°C")
    print(f"Most frequent temperature: {most_common_temp}°C (appeared {count} times)")
    print(f"3 lowest readings: {sorted_temps[:3]}")
    print(f"3 highest readings: {sorted_temps[-3:]}")
    
    range_temp = max_temp - min_temp
    print(f"Temperature range: {range_temp}°C")
    
    if range_temp < 10:
        print("Data looks stable 🌤️")
    else:
        print("Data shows high variation 🌡️")
    print("====================================")
    
    plt.figure(figsize=(8,5))
    plt.hist(clean_temps, bins=range(min_temp, max_temp + 1), edgecolor='black')
    plt.title("Temperature Distribution")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Frequency")
    plt.grid(alpha=0.3)
    plt.show()

sensor1 = [23, 25, 22, 27]
sensor2 = [24, 26, 'error', 28]
sensor3 = [22, None, 25, 23, 'error', 29]
sensor4 = [30, 31, 29, 'error', 28]

summarize_sensor_data(sensor1, sensor2, sensor3, sensor4)
