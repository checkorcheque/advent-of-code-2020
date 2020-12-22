# What is the highest seat ID on a boarding pass?

"""
ID legend
B = 1
F = 0
R = 1
L = 0
"""

with open("day5input.txt") as file:
    inputs = [line.strip("\n") for line in file.readlines()]

id_nums = []
for input in inputs:
    input = input.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0") #convert ID into bin num str
    input = (int(input[:7], 2) * 8) + (int(input[-3:], 2)) # find ID
    id_nums.append(input)

print(max(id_nums))
