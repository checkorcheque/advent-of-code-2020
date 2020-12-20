import re

#How many passwords are valid according to the new interpretation of the policies?

pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

correct_passwords = 0
with open("day2input.txt") as day2_file:
    for line in day2_file:
        match = pattern.search(line)
        first_location, second_location, character, password = match.groups()
        part1 = character == password[int(first_location) - 1]
        part2 = character == password[int(second_location) - 1]
        if part1 != part2:
            correct_passwords += 1
print(f"The number of correct passwords is {correct_passwords}")