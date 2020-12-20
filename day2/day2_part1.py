import re
#How many passwords are valid according to their policies

pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

correct_passwords = 0
with open("day2input.txt") as day2_file:
    for line in day2_file:
        value = 0
        match = pattern.search(line)
        minimum, maximum, character, password = match.groups()
        for letter in password:
            if letter == character:
                value += 1
        if value >= int(minimum) and value <= int(maximum):
            correct_passwords += 1

print(f"The number of correct passwords is {correct_passwords}")
