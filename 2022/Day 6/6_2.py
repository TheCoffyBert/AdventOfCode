res = 14
flag = 0

with open('input.txt') as input_txt:
    for line in input_txt:
        temp = line

        while flag < 1:
            curr = list(temp[:14])
            check = list(dict.fromkeys(curr))

            if len(curr) != len(check):
                res = res + 1
                temp = temp[1:]
            else:
                flag = 1

print(res)
