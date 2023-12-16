with open("input") as f:
    content = f.readlines()
    
def recursively_differ(sequence):
    if sequence[-1] == [0] * len(sequence[-1]):
        return 

    new_sequence = []
    for i, digit in enumerate(sequence[-1]):
        if i + 1 == len(sequence[-1]):
                break
        new_sequence.append(sequence[-1][i+1] - digit)
    sequence.append(new_sequence)
    recursively_differ(sequence)

def append_recursively(sequences):
    placeholder = 0
    for i, sequence in enumerate(sequences[::-1]):
        placeholder = sequence[0] - placeholder
        sequence.reverse()
        sequence.append(placeholder)
        sequence.reverse()

solution = 0

for line in content:
    digits = [int(digit) for digit in line.split()]
    sequence = [digits]
    recursively_differ(sequence)
    append_recursively(sequence)
    print(sequence)
    solution += sequence[0][0]

print(solution)


