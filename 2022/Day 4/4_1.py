sum = 0

with open('input.txt') as input_txt:
    for line in input_txt:
        a_b = line.split(',')

        a = a_b[0].split("-")
        min_a = int(a[0])
        max_a = int(a[1])

        b = a_b[1].split("-")
        min_b = int(b[0])
        max_b = int(b[1])

        if (min_a <= min_b and max_a >= max_b) or (min_b <= min_a and max_b >= max_a):
            sum = sum + 1

print(sum)