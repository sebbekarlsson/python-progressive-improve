sums = []

# (change) - store lines in variable again before looping
lines = open('input.txt').readlines()

# (change) - remove previous_num

previous_index = -1
for i in range(int(len(lines) / 2)):  # (change) divide the length of lines by 2
    current_index = previous_index + 1
    next_index = current_index + 1
    current_num = int(lines[current_index]) if current_index <= len(lines) -1 else 0
    next_num = int(lines[next_index]) if next_index <= len(lines) - 1 else 0

    sums.append(current_num + next_num)

    # (change) update previous index so that we always step 2 times ahead
    previous_index = next_index


print(sums)
