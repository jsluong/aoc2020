input = open('input/day2.txt', 'r').readlines()

# O(s); s is len of password
def isValid(minimum, maximum, char, password):
    count = password.count(char)
    return count >= int(minimum) and count <= int(maximum)

# O(n^2)
def partOne():
    valid = 0
    for line in input:
        rangeChar, char, password = str(line).split(" ")
        minimum, maximum = rangeChar.split("-")
        char = char[0]
        password = password[:-1]
        if isValid(minimum, maximum, char, password):
            valid += 1
    return valid

print("Part One:", partOne())
# print("Part Two:", partTwo())