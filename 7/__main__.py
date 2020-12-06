# (change) - a more functional approach

sums = []

lines = open('input.txt').readlines()

# calculating all of our positions in the loop in before hand
positions = list(map(lambda x: x * 2, range(int(len(lines) / 2))))
'''
positions variable will now contain:
[
    0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
    40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76,
    78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110,
    112, 114, 116, 118, 120, 122, 124, 126
]

Can you see the pattern?
We're always incrementing by 2.
This is because we are performing sum on pairs later.
'''

# great, now we have all of our positions, let's use them
for position in positions:
    current_num = int(lines[position])
    next_num = int(lines[min(len(lines) - 1, position + 1)])

    sums.append(current_num + next_num)

print(sums)
