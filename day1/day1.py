
nums = set()

with open("input.txt", "r") as file:
    for line in file:
        if (2020 - int(line)) in nums:
            print(int(line))
            print(2020 - int(line))
            print(int(line)*(2020-int(line)))
        nums.add(int(line))

