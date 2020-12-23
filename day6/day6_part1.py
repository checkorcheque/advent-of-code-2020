# For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

with open("day6input.txt") as file:
    responses = [response.replace("\n", "") for response in file.read().split("\n\n")]

groups_sum = 0
for response in responses:
    groups_sum += len("".join(set(response))) #set is used because it cannot have repeated values so it will ignore repeated values in string. join() bring the fixed string back together so its len can be found

print(groups_sum)