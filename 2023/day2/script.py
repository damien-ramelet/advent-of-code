with open("input") as f:
    content = f.readlines()

i_red = 12
i_green = 13
i_blue = 14
solution = 0

for line in content:
    game, sets = line.split(":")
    not_possible = False
    print(line)
    for _set in sets.split(";"):
        blue = 0
        red = 0
        green = 0
        for cubes in _set.split(","):
            cubes = cubes.strip()
            digit, color = cubes.split()
            if color == "blue":
                blue = int(digit)
                if blue > i_blue:
                    not_possible = True
            elif color == "red":
                red = int(digit)
                if red > i_red:
                    not_possible = True
            elif color == "green":
                green = int(digit)
                if green > i_green:
                    not_possible = True
        print(not_possible)
    if not_possible is False:
        game, digit = game.split()
        print(digit)
        solution += int(digit)

print(solution)


                

