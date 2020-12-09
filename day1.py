input = open('input/day1.txt', 'r')
lines = input.readlines()

table = set()
for line in lines:
    num = int(line)
    diff = 2020-num
    if diff not in table:
        table.add(num)
    else:
        print(diff, num, diff * num)