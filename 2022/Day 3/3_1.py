sum = 0

with open('input.txt') as input_txt:
    for line in input_txt:
        first = line[:len(line) // 2]
        second = line[len(line) // 2:]

        common_char = ''.join(set(first).intersection(second))
        if 97 <= ord(common_char) <= 122:
            sum = sum + (ord(common_char) - 96)
        elif 65 <= ord(common_char) <= 90:
            sum = sum + (ord(common_char) - 38)

print(sum)
