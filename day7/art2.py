data = {}

with open("input.txt", "r") as file:
    entries = [entry.strip()[:-1].replace("bags", "").replace("bag", "") for entry in file]
    entries = [[section.strip() for section in entry.split("contain")] for entry in entries]
    entries = [(entry[0], [section.strip() for section in entry[1].split(",")]) for entry in entries]
    for entry in entries:
        capacity = {}
        for element in entry[1]:
            if element == "no other":
                break
            num = element[0]
            color = element[2:]
            capacity[color] = int(num)
        data[entry[0]] = capacity

zz = {}

def total_capacity_outermost(color):
    return(sum([data[color][inner]*make_empty_bags_one(inner) for inner in data[color]]))

def total_capacity(color):
    if color in zz:
        return(zz[color])
    if not data[color]:
        zz[color] = 0
        return(0)
    return(1+sum([data[color][inner]*make_empty_bags_one(inner) for inner in data[color]]))

def make_empty_bags_one(inner):
    x = total_capacity(inner)
    if x == 0:
        return(1)
    return(x)

print(total_capacity_outermost("shiny gold"))
