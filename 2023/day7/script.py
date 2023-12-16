from collections import Counter
from functools import cmp_to_key

with open("input") as f:
    content = f.readlines()

five_kinds = []
four_kinds = []
full_houses = []
three_kinds = []
two_pairs = []
one_pairs = []
high_cards = []

def is_five_kind(line):
    counter = Counter(line.split()[0])
    if counter.most_common(1)[0][1] == 5:
        five_kinds.append(line)
        return True
    elif counter.most_common(1)[0][1] == 4 and counter["J"] == 4:
        five_kinds.append(line)
        return True
    elif counter.most_common(1)[0][1] == 4 and counter["J"] == 1:
        five_kinds.append(line)
        return True
    elif (counter.most_common(2)[0][1] == 3 and counter.most_common(2)[1][1] == 2) and counter["J"] == 3:
        five_kinds.append(line)
        return True
    elif (counter.most_common(2)[0][1] == 3 and counter.most_common(2)[1][1] == 2) and counter["J"] == 2:
        five_kinds.append(line)
        return True

def is_four_kind(line):
    hand = line.split()[0]
    counter = Counter(hand)
    if counter.most_common(1)[0][1] == 4:
        four_kinds.append(line)
        return True
    elif (counter.most_common(1)[0][1] == 3 and len(counter) == 3) and counter["J"] == 3:
        four_kinds.append(line)
        return True
    elif (counter.most_common(1)[0][1] == 3 and len(counter) == 3) and counter["J"] == 1:
        four_kinds.append(line)
        return True
    elif (counter.most_common(2)[0][1] == 2 and counter.most_common(2)[1][1] == 2) and counter["J"] == 2:
        four_kinds.append(line)
        return True

def is_full_house(line):
    hand = line.split()[0]
    counter = Counter(hand)
    if (counter.most_common(2)[0][1] == 3 and counter.most_common(2)[1][1] == 2):
        full_houses.append(line)
        return True
    elif (counter.most_common(2)[0][1] == 2 and counter.most_common(2)[1][1] == 2) and counter["J"] == 1:
        full_houses.append(line)
        return True

def is_three_kind(line):
    hand = line.split()[0]
    counter = Counter(hand)
    if counter.most_common(1)[0][1] == 3 and len(counter) == 3:
        three_kinds.append(line)
        return True
    elif counter.most_common(2)[0][1] == 2 and counter.most_common(2)[1][1] < 2 and counter["J"] == 1:
        three_kinds.append(line)
        return True
    elif counter.most_common(2)[0][1] == 2 and counter["J"] == 2:
        three_kinds.append(line)
        return True

def two_pair(line):
    hand = line.split()[0]
    counter = Counter(hand)
    if counter.most_common(2)[0][1] == 2 and counter.most_common(2)[1][1] == 2:
        two_pairs.append(line)
        return True

def one_pair(line):
    hand = line.split()[0]
    counter = Counter(hand)
    if counter.most_common(2)[0][1] == 2 and counter.most_common(2)[1][1] < 2:
        one_pairs.append(line)
        return True
    elif counter.total() == 5 and counter["J"] == 1:
        one_pairs.append(line)
        return True


def high_card(line):
    hand = line.split()[0]
    counter = Counter(hand)
    if counter.total() == 5:
        high_cards.append(line)
        return True


letters_to_rank = {"A": 1, "K": 2, "Q": 3, "T": 4}

def compare(left: str, right: str):
    left = left.split()[0]
    right = right.split()[0]
    for l, r in zip(left, right):
        if l == r:
            continue
        if r == "J":
            return -1
        if l == "J":
            return 1
        if not l.isdigit() and r.isdigit():
            return -1
        elif l.isdigit() and not r.isdigit():
            return 1
        elif l.isdigit() and r.isdigit():
            if int(l) > int(r):
                return -1
            return 1
        elif not l.isdigit() and not r.isdigit():
            if letters_to_rank[l] < letters_to_rank[r]:
                return -1
            return 1
    else:
        return 0


content = sorted(content, key=cmp_to_key(compare), reverse=True)
print(content)


for line in content:
    if not is_five_kind(line):
        if not is_four_kind(line):
            if not is_full_house(line):
                if not is_three_kind(line):
                    if not two_pair(line):
                        if not one_pair(line):
                            if not high_card(line):
                                print(line)
                                raise AssertionError()
print(five_kinds)
print(four_kinds)
print(full_houses)
print(three_kinds)
print(two_pairs)
print(one_pairs)
print(high_cards)

assert len(five_kinds) + len(four_kinds) + len(full_houses) + len(three_kinds) + len(two_pairs) + len(one_pairs) + len(high_cards) == len(content)

sorted_content = high_cards + one_pairs + two_pairs + three_kinds + full_houses + four_kinds + five_kinds
print(sorted_content)
solution = 0

for i, line in enumerate(sorted_content):
    score = int(line.split()[1])
    solution += (i+1)*score

print(solution)


