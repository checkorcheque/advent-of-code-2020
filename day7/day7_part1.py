#How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

with open("day7input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

def find_bag(color):
    all_colors = []
    final_colors = []

    total_colors = [line for line in lines if color in line and line.index(color) != 0]
    colors = [line[:line.index(" bags")] for line in total_colors]
    colors = [color for color in colors if color not in all_colors]
    
    for color in colors:
        all_colors.append(color)
        total_colors = find_bag(color)
        all_colors += total_colors

    for color in all_colors:
        if color not in final_colors:
            final_colors.append(color)
    return final_colors

print(len(find_bag("shiny gold")))
            