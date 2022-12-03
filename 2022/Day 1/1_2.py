temp_sum = 0
elves_cal = []
top_elves = [0,0,0]

with open('input.txt') as input_txt:
    for line in input_txt:
        if line == '\n':
            elves_cal.append(temp_sum)
            temp_sum = 0
        else:
            temp_sum = temp_sum + int(line)

if temp_sum != 0:
    elves_cal.append(temp_sum)

for i in range(len(elves_cal)):
    if elves_cal[i] > top_elves[0]:
        top_elves[2] = top_elves[1]
        top_elves[1] = top_elves[0]
        top_elves[0] = elves_cal[i]
    elif elves_cal[i] < top_elves[0] and elves_cal[i] > top_elves[1]:
        top_elves[2] = top_elves[1]
        top_elves[1] = elves_cal[i]
    elif elves_cal[i] < top_elves[1] and elves_cal[i] > top_elves[2]:
        top_elves[2] = elves_cal[i]

temp_sum = top_elves[0] + top_elves[1] + top_elves[2]
print(temp_sum)