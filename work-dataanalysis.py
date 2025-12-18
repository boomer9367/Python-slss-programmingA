# Data Analysis
# Author: Justin L
#
# 1. open the file and close it

filename = open("data")
filename.close()

# 2. count number of data points (rows minus header)
with open(filename, "r") as f:
    lines = f.readlines()

count = len(lines) - 1
print("Number of data points:", count)

# 3. average rainfall
total_rain = 0
rain_count = 0

# 4. average minimum temperature (F → C)
total_min_c = 0
min_count = 0

# 5. average maximum temperature in June
total_june_max = 0
june_count = 0


def is_number(s):
    # Check if string is a valid number (integer or decimal)
    s = s.strip()
    s = s.replace("-", "", 1)
    s = s.replace(".", "", 1)
    return s.isdigit()


for line in lines[1:]:
    parts = line.strip().split(",")

    if len(parts) < 6:
        continue

    if is_number(parts[1]):
        rain = float(parts[1])
        total_rain += rain
        rain_count += 1
    else:
        continue

    if is_number(parts[4]):
        temp_min_f = float(parts[4])
        temp_min_c = (temp_min_f - 32) * 5 / 9
        total_min_c += temp_min_c
        min_count += 1

    date = parts[0]
    if "-06-" in date and is_number(parts[5]):
        temp_max = float(parts[5])
        total_june_max += temp_max
        june_count += 1

# print results
print("Average rainfall (inches):", total_rain / rain_count)
print("Average minimum temperature (°C):", total_min_c / min_count)
print("Average maximum temperature in June (°F):", total_june_max / june_count)
