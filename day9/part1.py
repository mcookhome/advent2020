
with open("input.txt", "r") as file:
    entries = [int(entry) for entry in file]

def find_two(target, nums):
    passed = set()
    for num in nums:
        if (target - int(num)) in passed:
            return((int(num), (target - int(num))))
        passed.add(num)
    return(-1)

def xmas(psize, nums):
    i = 0  
    while i < len(nums):
        preamble = nums[i:i+psize]
        if find_two(nums[i+psize], preamble) == -1:
            return(nums[i+psize])
        i = i + 1
        
print(xmas(25, entries))
