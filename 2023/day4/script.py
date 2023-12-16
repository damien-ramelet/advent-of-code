import re

with open("input") as f:
    content = f.readlines()

total_point = 0

for line in content:
    current_point = 0
    winnings_numbers, own_numbers = line.split("|")
    parsed_winnings_numbers = [int(num) for num in re.match(r"Card\s+\d+: (.*)", winnings_numbers)[1].split()]

    parsed_own_numbers = [int(num) for num in own_numbers.split()]

    for own_number in parsed_own_numbers:
        if own_number in parsed_winnings_numbers:
            if current_point:
                current_point *= 2
            else:
                current_point += 1
    total_point += current_point

print(total_point)


#####

# 48760748 too high
# 18846087 too low
import re

with open("input") as f:
    content = f.readlines()

total_cards = 0
cards = []

for line in content:
    winnings_numbers, own_numbers = line.split("|")
    parsed_winnings_numbers = [int(num) for num in re.match(r"Card\s+\d+: (.*)", winnings_numbers)[1].split()]

    parsed_own_numbers = [int(num) for num in own_numbers.split()]
    cards.append((set(parsed_winnings_numbers), set(parsed_own_numbers)))



def parse_cards(cards: list[tuple[set[int], set[int]]], to_process: set[int] | None):
    how_many_cards = 0
    for i, (winnings_numbers, own_numbers) in enumerate(cards):
        if to_process is None:
            how_many_cards += 1
        if to_process is not None and not to_process:
            return how_many_cards

        if to_process:
            if i not in to_process:
                continue
            else:
                to_process.discard(i)

        offset = 1
        inner_to_process = set()

        for own_number in own_numbers:
            if own_number in winnings_numbers:
                inner_to_process.add(i+offset)
                how_many_cards += 1
                offset += 1
        if inner_to_process:
            how_many_cards += parse_cards(cards, to_process=inner_to_process)

    return how_many_cards

total_cards += parse_cards(cards, to_process=None)

print(total_cards)












