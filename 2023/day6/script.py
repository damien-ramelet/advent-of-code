import re
import math

with open("test_input") as f:
    content = f.read()
    
times = [int(time.strip()) for time in re.search(r".*Time:(?P<times>[\d\s\n]+)", content)["times"].split()]
distances = [int(distance.strip()) for distance in re.search(r".*Distance:(?P<distances>[\d\s\n]+)", content)["distances"].split()]

print(times)
print(distances)

race_way = 1

for t, d in zip(times, distances):
    way = 0
    for i in range(0, t):
        try_distance = (t-i)*i
        if try_distance > d:
            way += 1
    print(f"time: {t} - distance: {d}")
    print(f"race: {way}")
    race_way *= way

print(race_way)

race_way = 1

for time, distance in zip(times, distances):
    d1 = (-time + (time**2 - 4*(-1*-distance))**0.5)/(2*(-1))
    d2 = (-time - (time**2 - 4*(-1*-distance))**0.5)/(2*(-1))

    _min = math.ceil(min(d1, d2))
    if not _min*(time-_min) > distance:
        _min += 1
    _max = math.floor(max(d1, d2))
    if not _max*(time-_max) > distance:
        _max -= 1
    print(f"min button: {_min*(time-_min)} should be > to {distance}")
    print(f"max button: {_max*(time-_max)} should be > to {distance}")
    print(f"min: {_min} - max: {_max}")
    print(len(list(i for i in range(_min, _max+1))))
    race_way *= len(list(i for i in range(_min, _max+1)))
    print(race_way)

print(race_way)



