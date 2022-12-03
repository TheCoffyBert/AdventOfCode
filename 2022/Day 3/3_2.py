sum = 0

first = ''
second = ''
third = ''

counter = 1

with open('input.txt') as input_txt:
    for line in input_txt:
        if counter == 1:
            first = line[:-1]
            counter = counter + 1
        elif counter == 2:
            second = line[:-1]
            counter = counter + 1
        elif counter == 3:
            third = line[:-1]

            temp = ''.join(set(first).intersection(second))
            common_char = ''.join(set(temp).intersection(third))

            if 97 <= ord(common_char) <= 122:
                sum = sum + (ord(common_char) - 96)
            elif 65 <= ord(common_char) <= 90:
                sum = sum + (ord(common_char) - 38)

            counter = 1

print(sum)
