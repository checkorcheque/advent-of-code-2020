#How many individual bags are required inside your single shiny gold bag?

with open("day7input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

def bag_number(color):
    rule = ''
    for line in lines:
        if line[:line.index(" bags")] == color:
            rule = line

    if 'no' in rule:
        return 1
    
    
    rule = rule[rule.index('contain')+8:].split()

    total = 0
    i = 0
    while i < len(rule):
        number = int(rule[i])
        color = rule[i+1] + " " + rule[i+2]

        total += number * bag_number(color)

        i+=4
            
    return total + 1

count = bag_number("shiny gold") - 1 #added to subtract initial bag
print(count)