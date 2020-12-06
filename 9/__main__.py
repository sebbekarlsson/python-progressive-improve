lines = open('input.txt').readlines()

# (change) -  remove our global "positions" variable and just put it
# inside our "map" call.
sums = map(
    lambda position: int(lines[position]) +
    int(lines[min(len(lines) - 1, position + 1)]),
    list(map(lambda x: x * 2, range(int(len(lines) / 2))))
)

print(list(sums))
