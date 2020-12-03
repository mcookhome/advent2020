numbs = list()

with open("input.txt", "r") as file:
    for line in file:
        numbs.append(int(line))

def find_two(target, nums):
    passed = set()
    for num in nums:
        if (target - int(num)) in passed:
            print(int(num))
            print(target - int(num))
            print(int(num)*(target-int(num)))
            return((int(num), (target - int(num))))
        passed.add(num)

print(find_two(2020, numbs))

def find_three(target, nums):
    for i in range(len(nums)):
        temp = nums[:i]
        temp.extend(nums[i+1:])
        factors = find_two(target - nums[i], temp)
        if factors is not None:
            return(nums[i] * factors[0] * factors[1])

print(find_three(2020, numbs))
