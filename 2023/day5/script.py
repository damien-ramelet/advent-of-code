import re
#with open("test_input") as f:
#    content = f.read()
#
#print("####### TEST INPUT #####")

with open("input") as f:
    content = f.read()

seeds_ranges = [int(seed.strip()) for seed in re.search(r"seeds:(?P<seeds>[\d\s]+)", content)["seeds"].split()]
seeds_ranges_sorted = []
for i in range(0, len(seeds_ranges), 2):
    seeds_ranges_sorted.append([seeds_ranges[i], seeds_ranges[i+1]])
seeds_ranges_sorted.sort(key=sum)
seeds_ranges = [j for i in seeds_ranges_sorted for j in i]

seeds = (j for i in range(0, len(seeds_ranges), 2) for j in range(seeds_ranges[i], seeds_ranges[i] + seeds_ranges[i+1]))

seed_to_soil_map = [int(line.strip()) for line in re.search(r".*seed-to-soil map:\n(?P<map>[\d\s\n]+)", content)["map"].split()]
seeds_to_soil_map_sorted = []
for i in range(0, len(seed_to_soil_map), 3):
    seeds_to_soil_map_sorted.append([seed_to_soil_map[i], seed_to_soil_map[i+1], seed_to_soil_map[i+2]])
seeds_to_soil_map_sorted.sort(key=lambda l: l[1])
seed_to_soil_map = [j for i in seeds_to_soil_map_sorted for j in i]

soil_to_fertilazer_map = [int(line.strip()) for line in re.search(r".*soil-to-fertilizer map:\n(?P<map>[\d\s\n]+)", content)["map"].split()]
soil_to_fertilazer_map_sorted = []
for i in range(0, len(soil_to_fertilazer_map), 3):
    soil_to_fertilazer_map_sorted.append([soil_to_fertilazer_map[i], soil_to_fertilazer_map[i+1], soil_to_fertilazer_map[i+2]])
soil_to_fertilazer_map_sorted.sort(key=lambda l: l[1])
soil_to_fertilazer_map = [j for i in soil_to_fertilazer_map_sorted for j in i]

fertilizer_to_water_map = [int(line.strip()) for line in re.search(r".*fertilizer-to-water map:\n(?P<map>[\d\s\n]+)", content)["map"].split()]
fertilizer_to_water_map_sorted = []
for i in range(0, len(fertilizer_to_water_map), 3):
    fertilizer_to_water_map_sorted.append([fertilizer_to_water_map[i], fertilizer_to_water_map[i+1], fertilizer_to_water_map[i+2]])
fertilizer_to_water_map_sorted.sort(key=lambda l: l[1])
fertilizer_to_water_map = [j for i in fertilizer_to_water_map_sorted for j in i]

water_to_light_map = [int(line.strip()) for line in re.search(r".*water-to-light map:\n(?P<map>[\d\s\n]+)", content)["map"].split()]
water_to_light_map_sorted = []
for i in range(0, len(water_to_light_map), 3):
    water_to_light_map_sorted.append([water_to_light_map[i], water_to_light_map[i+1], water_to_light_map[i+2]])
water_to_light_map_sorted.sort(key=lambda l: l[1])
water_to_light_map = [j for i in water_to_light_map_sorted for j in i]

light_to_temperature_map = [int(line.strip()) for line in re.search(r".*light-to-temperature map:\n(?P<map>[\d\s\n]+)", content)["map"].split()]
light_to_temperature_map_sorted = []
for i in range(0, len(light_to_temperature_map), 3):
    light_to_temperature_map_sorted.append([light_to_temperature_map[i], light_to_temperature_map[i+1], light_to_temperature_map[i+2]])
light_to_temperature_map_sorted.sort(key=lambda l: l[1])
light_to_temperature_map = [j for i in light_to_temperature_map_sorted for j in i]

temperature_to_humidity_map = [int(line.strip()) for line in re.search(r".*temperature-to-humidity map:\n(?P<map>[\d\s\n]+)", content)["map"].split()]
temperature_to_humidity_map_sorted =[]
for i in range(0, len(temperature_to_humidity_map), 3):
    temperature_to_humidity_map_sorted.append([temperature_to_humidity_map[i], temperature_to_humidity_map[i+1], temperature_to_humidity_map[i+2]])
temperature_to_humidity_map_sorted.sort(key=lambda l: l[1])
temperature_to_humidity_map = [j for i in temperature_to_humidity_map_sorted for j in i]

humidity_to_location_map = [int(line.strip()) for line in re.search(r".*humidity-to-location map:\n(?P<map>[\d\s\n]+)", content)["map"].split()]
humidity_to_location_map_sorted = []
for i in range(0, len(humidity_to_location_map), 3):
    humidity_to_location_map_sorted.append([humidity_to_location_map[i], humidity_to_location_map[i+1], humidity_to_location_map[i+2]])
humidity_to_location_map_sorted.sort(key=lambda l: l[1])
humidity_to_location_map = [j for i in humidity_to_location_map_sorted for j in i]
 

locations = []

def map_seed_to_soil(seed: int):
    for i in range(0, len(seed_to_soil_map), 3):
        destination = seed_to_soil_map[i]
        source = seed_to_soil_map[i+1]
        _range = seed_to_soil_map[i+2]
        if not source <= seed <= source + _range - 1:
            continue
        else:
            d = destination-source
            return seed + d
    else:
        return seed

def map_soil_to_fertilazer(seed: int):
    for i in range(0, len(soil_to_fertilazer_map), 3):
        destination = soil_to_fertilazer_map[i]
        source = soil_to_fertilazer_map[i+1]
        _range = soil_to_fertilazer_map[i+2]
        if not source <= seed <= source + _range - 1:
            continue
        else:
            d = destination-source
            return seed + d
    else:
        return seed

def map_fertilazer_to_water(seed: int):
    for i in range(0, len(fertilizer_to_water_map), 3):
        destination = fertilizer_to_water_map[i]
        source = fertilizer_to_water_map[i+1]
        _range = fertilizer_to_water_map[i+2]
        if not source <= seed <= source + _range - 1:
            continue
        else:
            d = destination-source
            return seed + d
    else:
        return seed


def map_water_to_light(seed: int):
    for i in range(0, len(water_to_light_map), 3):
        destination = water_to_light_map[i]
        source = water_to_light_map[i+1]
        _range = water_to_light_map[i+2]
        if not source <= seed <= source + _range - 1:
            continue
        else:
            d = destination-source
            return seed + d
    else:
        return seed

def map_light_to_temperature(seed: int):
    for i in range(0, len(light_to_temperature_map), 3):
        destination = light_to_temperature_map[i]
        source = light_to_temperature_map[i+1]
        _range = light_to_temperature_map[i+2]
        if not source <= seed <= source + _range - 1:
            continue
        else:
            d = destination-source
            return seed + d
    else:
        return seed

def map_temperature_to_humidity(seed: int):
    for i in range(0, len(temperature_to_humidity_map), 3):
        destination = temperature_to_humidity_map[i]
        source = temperature_to_humidity_map[i+1]
        _range = temperature_to_humidity_map[i+2]
        if not source <= seed <= source + _range - 1:
            continue
        else:
            d = destination-source
            return seed + d
    else:
        return seed


def map_humidity_to_location(seed: int):
    for i in range(0, len(humidity_to_location_map), 3):
        destination = humidity_to_location_map[i]
        source = humidity_to_location_map[i+1]
        _range = humidity_to_location_map[i+2]
        if not source <= seed <= source + _range - 1:
            continue
        else:
            d = destination-source
            return seed + d
    else:
        return seed




#for seed in seeds:
#    soil = map_seed_to_soil(seed)
#    fertilazer = map_soil_to_fertilazer(soil)
#    water = map_fertilazer_to_water(fertilazer)
#    light = map_water_to_light(water)
#    temperature = map_light_to_temperature(light)
#    humidity = map_temperature_to_humidity(temperature)
#    location = map_humidity_to_location(humidity)
#    locations.append(location)

#print(min(locations))
print(min(map_humidity_to_location(map_temperature_to_humidity(map_light_to_temperature(map_water_to_light(map_fertilazer_to_water(map_soil_to_fertilazer(map_seed_to_soil(seed))))))) for seed in seeds))
