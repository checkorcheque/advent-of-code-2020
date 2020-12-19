# what is the product of the three entries that sum to 2020?
# turn .txt into a list of nums
with open("day1input.txt") as day1_file:
    inputs = [int(num) for num in day1_file]

for num1 in inputs:
    for num2 in inputs:
        for num3 in inputs:
            if num1 + num2 + num3 == 2020:
                product = (num1 * num2 * num3)
                
print(product)
