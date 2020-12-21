#Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

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
print(num_of_trees(3,1))