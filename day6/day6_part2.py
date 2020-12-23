numbered_responses = {}
with open("day6input.txt") as file:
    for response in file.read().split("\n\n"):
        print(response)
        print(response.count("\n"))
        numbered_responses[response.replace("\n", "")] = response.count("\n") + 1 # "+ 1" is needed b/c I am losing 1 \n when I split the lines
        
#print(numbered_responses)


alphabet = "abcdefghijklmnopqrstuvwxyz"
print(len(alphabet))
groups_sum = 0
individual_sum = 0
for response in numbered_responses.keys():
    groups_sum += len("".join(set(response))) #set is used because it cannot have repeated values so it will ignore repeated values in string. join() bring the fixed string back together so its len can be found
    for letter in alphabet:
        if response.count(letter) == numbered_responses[response]:
            individual_sum += 1

print(groups_sum)
print(individual_sum)
