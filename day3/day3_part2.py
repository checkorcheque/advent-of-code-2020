'''Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.'''

with open("day3input.txt") as file:
    path = [line.strip() for line in file.readlines()]

def num_of_trees(vectorX, vectorY):
    x, y, trees = 0, 0, 0
    while y < len(path) - 1:
        x += vectorX
        y += vectorY
        if path[y][x % len(path[y])] == "#":
            trees += 1
    return trees

print(num_of_trees(1,1) * num_of_trees(3,1) * num_of_trees(5,1) * num_of_trees(7,1) * num_of_trees(1,2))
