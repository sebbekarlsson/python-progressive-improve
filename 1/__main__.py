my_file = open('input.txt')
contents = my_file.read()
lines = contents.split('\n')

sum_pairs = []
sums = []

previous_num = None
for line in lines:
    num = int(line)

    if previous_num:
        sum_pairs.append((previous_num, num))
        num = None

    previous_num = num


for pair in sum_pairs:
    sums.append(pair[0] + pair[1])

print(sums)
