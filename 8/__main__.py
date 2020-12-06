lines = open('input.txt').readlines()

positions = list(map(lambda x: x * 2, range(int(len(lines) / 2))))

# (change) -  remove our for loop and use "map" instead.
sums = map(
    lambda position: int(lines[position]) +
    int(lines[min(len(lines) - 1, position + 1)]), positions
)

print(list(sums))
