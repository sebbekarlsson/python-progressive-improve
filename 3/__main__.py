my_file = open('input.txt')

lines = my_file.readlines()

sums = []

previous_num = None
for line in lines:
    num = int(line)

    if previous_num:
        # (change) - remove second loop & sum_pairs variable and calculate
        # sum in our main loop instead
        sums.append(previous_num + num)
        num = None

    previous_num = num


print(sums)
