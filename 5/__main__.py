sums = []

# (change) - call .readlines directly in the loop declaration
previous_num = None
for line in open('input.txt').readlines():
    num = int(line)

    if previous_num:
        sums.append(previous_num + num)
        num = None

    previous_num = num


print(sums)
