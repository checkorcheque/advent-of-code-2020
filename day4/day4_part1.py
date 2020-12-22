import re
#Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

valid =  0
lst = []
data = []
with open("day4input.txt") as file:
    lst = [line.replace("\n", " ").strip().split(" ") for line in file.read().split("\n\n")] #seperate each value in input into a string in a list while simultaneously removing and replacing newlines and removing trailing and leading whitespace
    for string in lst:
        dicts = {} #used to ensure that each set of values is seperated into its own dict
        for keyvalues in string:
            keyvalue = keyvalues.split(":")
            key, value = keyvalue[0], keyvalue[1]
            dicts[key] = value
        data.append(dicts)

for dicts in data:
    if set(("ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt")).issubset(dicts):
        valid += 1

print(valid)