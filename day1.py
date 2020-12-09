input = open('input/day1.txt', 'r').readlines()
numbers = [int(line) for line in input]

# O(n)
def partOne(target=2020, numbers=numbers):
    table = set()
    for num in numbers:
        diff = target-num
        if diff not in table:
            table.add(num)
        else:
            return diff * num

# O(n^2)
def partTwo(target=2020, numbers=numbers):
    for i, number in enumerate(numbers):
        searchTarget = target-number
        attempt = partOne(searchTarget, numbers[i:])
        if attempt:
            return attempt * number

print("Part One:", partOne())
print("Part Two:", partTwo())