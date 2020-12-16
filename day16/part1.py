import itertools
with open("input.txt", "r") as file:
    entries = [entry.strip() for entry in file.read().split('\n\n')]
    categories = [entry.split(":") for entry in entries[0].split('\n')]
    ranges = [[cat[1].split(" ")[1], cat[1].split(" ")[3]] for cat in categories]
    ranges = sum(ranges, [])
    ranges = [list(range(int(r.split("-")[0]), int(r.split("-")[1])+1)) for r in ranges]
    all_valid = set(sum(ranges, []))
    nearby = [entry.split(",") for entry in entries[2].split('\n')[1:]]    
    nearby = [[int(val) for val in x] for x in nearby]
    invalid_nums = [[val for val in x if val not in all_valid] for x in nearby]
    print(sum(sum(invalid_nums, [])))
