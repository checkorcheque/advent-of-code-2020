#find the two entries that sum to 2020 and then multiply those two numbers together.

#turn .txt into a list of nums
with open("day1input_part1.txt", "r") as day1_file:
    inputs = [int(num) for num in day1_file]

for num1 in inputs:
    for num2 in inputs:
        if num1 + num2 == 2020:
            print(f"num1 is {num1} and num2 is {num2}")
            print(f"num1 * num2 is {num1 * num2}")


