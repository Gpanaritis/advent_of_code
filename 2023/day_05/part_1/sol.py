with open("data.txt", "r") as f:
    lines = f.readlines()

seeds = []
soil = []
fertilizer = []
water = []
light = []
temperature = []
humidity = []
location = []

whitespace_count = 0

for line in lines:
    if line == "\n":
        whitespace_count += 1
    elif whitespace_count == 0:
        seeds = line.split(": ")[1].strip().split(" ")
    elif whitespace_count == 1:
        soil.append(line.strip().split(" "))
    elif whitespace_count == 2:
        fertilizer.append(line.strip().split(" "))
    elif whitespace_count == 3:
        water.append(line.strip().split(" "))
    elif whitespace_count == 4:
        light.append(line.strip().split(" "))
    elif whitespace_count == 5:
        temperature.append(line.strip().split(" "))
    elif whitespace_count == 6:
        humidity.append(line.strip().split(" "))
    elif whitespace_count == 7:
        location.append(line.strip().split(" "))

seeds = [int(i) for i in seeds]
soil_seeds = [0] * len(seeds)
fertilizer_seeds = [0] * len(seeds)
water_seeds = [0] * len(seeds)
light_seeds = [0] * len(seeds)
temperature_seeds = [0] * len(seeds)
humidity_seeds = [0] * len(seeds)
location_seeds = [0] * len(seeds)

for i in range(1, len(soil)):
    for j in range(len(seeds)):
        if int(seeds[j]) >= int(soil[i][1]) and int(seeds[j]) < int(soil[i][1]) + int(soil[i][2]) and soil_seeds[j] == 0:
            soil_seeds[j] = int(soil[i][0]) + int(seeds[j]) - int(soil[i][1])
for i in range(len(soil_seeds)):
    if soil_seeds[i] == 0:
        soil_seeds[i] = seeds[i]

           
for i in range(1, len(fertilizer)):
    for j in range(len(seeds)):
        if soil_seeds[j] >= int(fertilizer[i][1]) and soil_seeds[j] < int(fertilizer[i][1]) + int(fertilizer[i][2]) and fertilizer_seeds[j] == 0:
            fertilizer_seeds[j] = int(fertilizer[i][0]) + int(soil_seeds[j]) - int(fertilizer[i][1])
for i in range(len(fertilizer_seeds)):
    if fertilizer_seeds[i] == 0:
        fertilizer_seeds[i] = soil_seeds[i]


for i in range(1, len(water)):
    for j in range(len(seeds)):
        if fertilizer_seeds[j] >= int(water[i][1]) and fertilizer_seeds[j] < int(water[i][1]) + int(water[i][2]) and water_seeds[j] == 0:
            water_seeds[j] = int(water[i][0]) + int(fertilizer_seeds[j]) - int(water[i][1])
for i in range(len(water_seeds)):
    if water_seeds[i] == 0:
        water_seeds[i] = fertilizer_seeds[i]

for i in range(1, len(light)):
    for j in range(len(seeds)):
        if water_seeds[j] >= int(light[i][1]) and water_seeds[j] < int(light[i][1]) + int(light[i][2]) and light_seeds[j] == 0:
            light_seeds[j] = int(light[i][0]) + int(water_seeds[j]) - int(light[i][1])
for i in range(len(light_seeds)):
    if light_seeds[i] == 0:
        light_seeds[i] = water_seeds[i]

for i in range(1, len(temperature)):
    for j in range(len(seeds)):
        if light_seeds[j] >= int(temperature[i][1]) and light_seeds[j] < int(temperature[i][1]) + int(temperature[i][2]) and temperature_seeds[j] == 0:
            temperature_seeds[j] = int(temperature[i][0]) + int(light_seeds[j]) - int(temperature[i][1])
for i in range(len(temperature_seeds)):
    if temperature_seeds[i] == 0:
        temperature_seeds[i] = light_seeds[i]

for i in range(1, len(humidity)):
    for j in range(len(seeds)):
        if temperature_seeds[j] >= int(humidity[i][1]) and temperature_seeds[j] < int(humidity[i][1]) + int(humidity[i][2]) and humidity_seeds[j] == 0:
            humidity_seeds[j] = int(humidity[i][0]) + int(temperature_seeds[j]) - int(humidity[i][1])
for i in range(len(humidity_seeds)):
    if humidity_seeds[i] == 0:
        humidity_seeds[i] = temperature_seeds[i]

for i in range(1, len(location)):
    for j in range(len(seeds)):
        if humidity_seeds[j] >= int(location[i][1]) and humidity_seeds[j] < int(location[i][1]) + int(location[i][2]) and location_seeds[j] == 0:
            location_seeds[j] = int(location[i][0]) + int(humidity_seeds[j]) - int(location[i][1])
for i in range(len(location_seeds)):
    if location_seeds[i] == 0:
        location_seeds[i] = humidity_seeds[i]

print(min(location_seeds))