my_file = open('input.txt')

# (change) - use .readlines instead of split('\n')
lines = my_file.readlines()

sum_pairs = []
sums = []

previous_num = None
for line in lines:
    num = int(line)

    if previous_num:
        sum_pairs.append((previous_num, num))
        num = None

    previous_num = num


# (change) - use tuple unwrapping (a, b) instead of pair[0] and pair[1]
for a, b in sum_pairs:
    sums.append(a + b)

print(sums)
