stacks = [
    ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'],
    ['S', 'W', 'C'],
    ['R', 'Z', 'T', 'M'],
    ['D', 'T', 'C', 'H', 'S', 'P', 'V'],
    ['G', 'P', 'T', 'L', 'D', 'Z'],
    ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D'],
    ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R'],
    ['L', 'H', 'R', 'B', 'T', 'V', 'M'],
    ['Q', 'P', 'D', 'S', 'V']
]

res = ''

with open('input_s.txt') as input_s:
    for line in input_s:
        data = line.split(' ')

        index = int(data[1])
        stack_from = int(data[3]) - 1
        stack_to = int(data[5]) - 1

        for x in range(index):
            stacks[stack_to].append(stacks[stack_from].pop())

for x in range(9):
    res = res + stacks[x].pop()

print(res)
