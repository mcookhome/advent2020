from functools import reduce

def possible(lon, valid_set):
    return(all([num in valid_set for num in lon]))
    
def ins(d, key, count):
    if key in d:
        d[key].append(count)
    else:
        d[key] = [count]

def max_len(poss):
    return(max([len(poss[i]) for i in poss]))
    
def remove_all(poss, cat):
    for c in poss:
        y = poss[c]
        if cat in y:
            poss[c].remove(cat)
        poss[c] = y        
    return(poss)

def mappings(poss):
    d = {}
    while max_len(poss) > 0:
        for i in poss:
            if len(poss[i]) == 1:
                cat = poss[i][0]
                d[cat] = i
                poss = remove_all(poss, cat)
    return(d)
    
with open("input.txt", "r") as file:
    entries = [entry.strip() for entry in file.read().split('\n\n')]
    categories = [entry.split(":") for entry in entries[0].split('\n')]
    ranges = [[cat[1].split(" ")[1], cat[1].split(" ")[3]] for cat in categories]
    cats = {}
    for cat in categories:
        field = cat[0]
        cats[field] = [cat[1].split(" ")[1], cat[1].split(" ")[3]]
        cats[field] = [list(range(int(r.split("-")[0]), int(r.split("-")[1])+1)) for r in cats[field]]    
        cats[field] = set(sum(cats[field],[]))
    ranges = sum(ranges, [])
    ranges = [list(range(int(r.split("-")[0]), int(r.split("-")[1])+1)) for r in ranges]
    all_valid = set(sum(ranges, []))
    nearby = [entry.split(",") for entry in entries[2].split('\n')[1:]]    
    nearby = [[int(val) for val in x] for x in nearby]
    invalid_nums = [(x, [val for val in x if val not in all_valid]) for x in nearby]
    valid_entries = [entry for entry, invalid in invalid_nums if len(invalid) == 0]
    fields = {}
    for i in range(len(valid_entries[0])):
        fields[i] = [entry[i] for entry in valid_entries]
    poss_mappings = {}
    for i in fields:
        for cat in cats:
             if possible(fields[i], cats[cat]): 
                 ins(poss_mappings, i, cat)
    tru = mappings(poss_mappings)
    print(tru)
    departures = [tru[cat] for cat in tru if 'departure' in cat]
    my_ticket = [entry.split(",") for entry in entries[1].split('\n')[1:]][0]
    my_dep_vals = [int(my_ticket[i]) for i in departures]
    print(reduce((lambda x, y: x * y), my_dep_vals)) 
