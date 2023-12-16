with open("input") as f:
    content = f.readlines()

solution = 0

for line in content:
    line_digit = ""
    left_number = ""
    right_number = ""
    for char in line:
        if char.isdigit():
            if not left_number:
                left_number = char
            right_number = char
    line_digit = left_number + right_number
    solution += int(line_digit)

print(solution)

