points = 0

with open('input.txt') as input_txt:
    for line in input_txt:
        match = line.split(' ')
        print(match)
        if match[0] == 'A':
            if match[1] == 'X\n':
                points = points + 4
            elif match[1] == 'Y\n':
                points = points + 8
            elif match[1] == 'Z\n':
                points = points + 3
        elif match[0] == 'B':
            if match[1] == 'X\n':
                points = points + 1
            elif match[1] == 'Y\n':
                points = points + 5
            elif match[1] == 'Z\n':
                points = points + 9
        elif match[0] == 'C':
            if match[1] == 'X\n':
                points = points + 7
            elif match[1] == 'Y\n':
                points = points + 2
            elif match[1] == 'Z\n':
                points = points + 6

print(points)