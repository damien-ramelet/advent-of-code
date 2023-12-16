with open("input") as f:
    content = f.readlines()

solution = 0

for line in content:
    max_blue = 0
    max_green = 0
    max_red = 0
    game, sets = line.split(":")
    print(line)
    for _set in sets.split(";"):
        for cubes in _set.split(","):
            cubes = cubes.strip()
            digit, color = cubes.split()
            if color == "blue":
                blue = int(digit)
                if blue > max_blue:
                    max_blue = blue
            elif color == "red":
                red = int(digit)
                if red > max_red:
                    max_red = red
            elif color == "green":
                green = int(digit)
                if green > max_green:
                    max_green = green
                    
    power = max_green * max_blue * max_red
    print(f"blue: {max_blue} - green: {max_green} - red: {max_red}")
    solution += power


print(solution)


                

