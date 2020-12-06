# (change) - use open('input.txt').readlines() directly instead of
# storing the file in a variable first.
lines = open('input.txt').readlines()

sums = []

previous_num = None
for line in lines:
    num = int(line)

    if previous_num:
        sums.append(previous_num + num)
        num = None

    previous_num = num


print(sums)
