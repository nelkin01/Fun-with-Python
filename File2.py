sensor1 = [23, 25, 22, 27]
sensor2 = [24, 26, 'error', 28]
sensor3 = [22, None, 25, 23]


all_temps = sensor1 + sensor2 + sensor3
print("All sensor data:", all_temps)


valid_temps = [t for t in all_temps if isinstance(t, (int, float))]
print("Valid temperature readings:", valid_temps)


min_temp = min(valid_temps)
max_temp = max(valid_temps)
avg_temp = sum(valid_temps) / len(valid_temps)

print(f"Minimum temperature: {min_temp}")
print(f"Maximum temperature: {max_temp}")
print(f"Average temperature: {round(avg_temp, 2)}")
