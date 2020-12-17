import itertools
posns = set()

with open("input.txt", "r") as file:
    entries = [entry.strip() for entry in file]
    for y in range(len(entries)):
        for x in range(len(entries[0])):
            if entries[y][x] == '#':
                posns.add((x,y,0))

def neighbors(pos):
    opts = (-1,0,1)
    rels = list(itertools.product(opts,opts,opts)) 
    rels.remove((0,0,0))
    abss = [(x+pos[0], y+pos[1], z+pos[2]) for x,y,z in rels]
    return(abss)

def active_neighbors(pos, d):
    return(sum([p in d for p in neighbors(pos)]))

def get_x_range(posns):
    xs = [x for x,y,z in posns]
    return(range(min(xs)-1, max(xs)+2))

def get_y_range(posns):
    ys = [y for x,y,z in posns]
    return(range(min(ys)-1, max(ys)+2))

def get_z_range(posns):
    zs = [z for x,y,z in posns]
    return(range(min(zs)-1, max(zs)+2))

def one_iteration(d):
    p = set()
    for x in get_x_range(d):
        for y in get_y_range(d):
            for z in get_z_range(d):
                pos = (x,y,z)
                ns = active_neighbors(pos, d)
                if pos in d:
                    if ns == 2 or ns == 3:
                        p.add(pos)
                else:
                    if ns == 3:
                        p.add(pos)
    return(p)

def x_iterations(x, d):
    count = 0
    while count < x:
        d = one_iteration(d)
        count = count + 1
    return(len(d))

print(x_iterations(6,posns))
