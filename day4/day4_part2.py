import re
#Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
"""byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not."""

length = 0
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
        if 1920 <= int(dicts["byr"]) <= 2002:
            if 2010 <= int(dicts["iyr"]) <= 2020:
                if 2020 <= int(dicts["eyr"]) <= 2030:
                    if (dicts["hgt"][-2:] == "cm") and (150 <= int(dicts["hgt"].replace("in","").replace("cm","")) <= 193) or ((dicts["hgt"])[-2:] == "in") and (59 <= int(dicts["hgt"].replace("in","").replace("cm","")) <= 76):
                        if re.match(r'#[^g-z]{6}', dicts["hcl"]) != None:
                            if len(dicts["ecl"]) == 3 and dicts["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                                if re.match(r"^\d{9}$", dicts["pid"]) != None and len(dicts["pid"]) == 9:
                                    valid += 1
                   
print(valid)