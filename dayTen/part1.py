
with open("input.txt", "r") as file:
    entries = [int(entry) for entry in file]
    entries = sorted(entries)
    print(entries)

def adapter(jolts):
    one = 1
    two = 0
    three = 1
    for i in range(len(jolts) - 1):
        diff = jolts[i+1] - jolts[i]
        if diff == 1:
             one = one + 1
        elif diff == 2:
             two = two + 1
        elif diff == 3:
             three = three + 1
    return(one*three)

print(adapter(entries))
