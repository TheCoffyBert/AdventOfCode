temp_sum = 0
elves_cal = []

with open('input_1_1.txt') as input_1_1:
    for line in input_1_1:
        if line == '\n':
            elves_cal.append(temp_sum)
            temp_sum = 0
        else:
            temp_sum = temp_sum + int(line)

if temp_sum != 0:
    elves_cal.append(temp_sum)

temp_sum = elves_cal[0]

for i in range(len(elves_cal)):
    if temp_sum < elves_cal[i]:
        temp_sum = elves_cal[i]

print(temp_sum)