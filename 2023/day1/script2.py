from functools import reduce
from operator import add

with open("input") as f:
    content = f.readlines()

solution = 0
spelled_digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
line_digits = []

for line in content:
    print(line)

    line_digit = ""
    left_number = ""
    right_number = ""

    i = 0
    while i <= len(line):
        try:
            if line[i:i+3] in spelled_digits:
              line = line[:i] + spelled_digits[line[i:i+3]] * 2 + line[i:i+3][-1] + line[i+3:]
            if line[i:i+4] in spelled_digits:
                line = line[:i] + spelled_digits[line[i:i+4]] * 3 + line[i:i+4][-1] + line[i+4:]
            if line[i:i+5] in spelled_digits:
                line = line[:i] + spelled_digits[line[i:i+5]] * 4 + line[i:i+5][-1] + line[i+5:]
        except:
            break
        i += 1

    print(line)


    for char in line:
        if char.isdigit():
            if not left_number:
                left_number = char
            right_number = char
    line_digit = left_number + right_number
    print(line_digit)
    solution += int(line_digit)
    line_digits.append(line_digit)

print(solution)
print(line_digits)
print(reduce(add, [int(i) for i in line_digits]))

# 12one9
# 1twoone9
