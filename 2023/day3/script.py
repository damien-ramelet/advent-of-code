import random
with open("input") as f:
    content = f.read()

symbols_coordinates: list[tuple] = []
digits_coordinates: dict[tuple, int] = {}

solution = 0

current_digit = ""
not_symbols = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "\n"}

#def is_not_adjacent(number, content, i):
#    """
#    Given coordinates of the last digit of a number,
#    the number is not adjacent if:
#        - No symbols before the first digit
#        - No symbols after the last digit
#        - No symbols in [-141, -141+(len of the number)+1] window:
#                  *****
#                   123
#        - No symbols in [141-(len of the number)-1, 141+1] window:
#                   123
#                  *****
#    """
##    if number == "378":
##        import pdb; pdb.set_trace()
#    len_of_the_number = len(number)
#    has_no_symbols_after = content[i] in (".", "\n")
#    #print(f"{number} ({i}) has_no_symbols_after: {has_no_symbols_after}", end=" - ")
#    has_no_symbols_before = content[i-(len_of_the_number+1)] in (".", "\n")
#    chars_upper = content[i-141-len_of_the_number-1:i-141+1]
#    has_no_symbols_upper = len([char for char in chars_upper if char in not_symbols]) == len(chars_upper)
#    chars_lower = content[i+(141-len_of_the_number)-1:i+141+1]
#    has_no_symbols_lower = len([char for char in chars_lower if char in not_symbols]) == len(chars_lower)
#    #print(f"has_no_symbols_lower: {has_no_symbols_lower}")
#    if has_no_symbols_after and has_no_symbols_before and has_no_symbols_upper and has_no_symbols_lower:
#        return True
#    return False
#
#
#current_line = ""
#for i, char in enumerate(content):
#    if char.isdigit():
#        current_digit += char
#    elif current_digit != "":
#        line = i//141
#        position_in_line = i - line * 141
#        #print(f"Digit {current_digit} can be found at position {(line, position_in_line)}")
#        if not is_not_adjacent(current_digit, content, i):
#            print(f"{current_digit} at position {(line, position_in_line)} is adjacent to a symbols")
#            solution += int(current_digit)
#        current_digit = ""
#print(solution)
#


def is_not_adjacent(number, content, i):
    """
    Given coordinates of the last digit of a number,
    the number is not adjacent if:
        - No symbols before the first digit
        - No symbols after the last digit
        - No symbols in [-141, -141+(len of the number)+1] window:
                  *****
                   123
        - No symbols in [141-(len of the number)-1, 141+1] window:
                   123
                  *****
    """
#    if number == "378":
#        import pdb; pdb.set_trace()
    len_of_the_number = len(number)
    has_no_symbols_after = content[i] in (".", "\n")
    #print(f"{number} ({i}) has_no_symbols_after: {has_no_symbols_after}", end=" - ")
    has_no_symbols_before = content[i-(len_of_the_number+1)] in (".", "\n")
    chars_upper = content[i-141-len_of_the_number-1:i-141+1]
    has_no_symbols_upper = len([char for char in chars_upper if char in not_symbols]) == len(chars_upper)
    chars_lower = content[i+(141-len_of_the_number)-1:i+141+1]
    has_no_symbols_lower = len([char for char in chars_lower if char in not_symbols]) == len(chars_lower)
    #print(f"has_no_symbols_lower: {has_no_symbols_lower}")
    if has_no_symbols_after and has_no_symbols_before and has_no_symbols_upper and has_no_symbols_lower:
        return True
    return False

solution = 0
position_to_gears = {}
position_to_numbers = {}
current_line = ""
for i, char in enumerate(content):
    line = i//141
    position_in_line = i - line * 141
    if char.isdigit():
        if content[i-1] == "-":
            current_digit += f"-{char}"
        else:
            current_digit += f"{char}"
    elif char == "*":
        position_to_gears[i] = "*"
        if current_digit:
            _id = random.randint(1, 10000000)
            for j, _ in enumerate(current_digit):
                position_to_numbers[(i-1)-j] = _id, int(current_digit)
            current_digit = ""
        #print(f"Digit {current_digit} can be found at position {(line, position_in_line)}")
    else:
        if current_digit:
            _id = random.randint(1, 100000000)
            for j, _ in enumerate(current_digit):
                position_to_numbers[(i-1)-j] = _id, int(current_digit)
            current_digit = ""

for i in position_to_gears:
    line = i//141
    position_in_line = i - line * 141
#    if line == 138 or line == 126:
#        import pdb; pdb.set_trace()
    values = set()
    try:
        values.add(position_to_numbers[i-1])
    except:
        pass
    try:
        values.add(position_to_numbers[i+1])
    except:
        pass

    for j in range(i-141-1, i-141+2):
        try:
            values.add(position_to_numbers[j])
        except:
            pass

    for j in range(i+141-1, i+141+2):
        try:
            values.add(position_to_numbers[j])
        except:
            pass

    result = 1
    if len(values) > 2:
        print("TTTTTTTTTTTTTT")
    if len(values) >= 2:
        for value in values:
            result *= value[1]
        print(values, result, solution)
        solution += result

    #print(f"""Found adjacent gears on line {i//141 + 1}: {values}""")
   # print(f"Not adjacent gears on line {i//141 +1} - {position_in_line + 1}")
    #if set(value[1] for value in values) == 1:
     #   print(values, line + 1)



print(solution)



