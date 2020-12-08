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
    print(data)

zz = {}

def can_contain_shiny_gold(color):
    if color in zz:
        return(zz[color])
    if data[color] is None:
        zz[color] = False
        return(False)
    if "shiny gold" in data[color]:
        zz[color] = True
        return(True)
    return(any([can_contain_shiny_gold(bag) for bag in data[color]])) 

print(sum([can_contain_shiny_gold(color) for color in data]))
