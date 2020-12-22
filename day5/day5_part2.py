# What is the ID of your seat?

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

id_nums.sort()
for i in range(len(id_nums)-1):
    if id_nums[i+1] - id_nums[i] == 2: # My ID has to be in between 2 of the IDs in the id_nums list, so the difference between these numbers must be 2
        print(id_nums[i] + 1)


