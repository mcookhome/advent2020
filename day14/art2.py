
with open("input.txt", "r") as file:
    entries = [entry.strip() for entry in file]

def choose_bit(pair):
    if pair[0] in 'X1':
        return(pair[0])
    else:
        return(pair[1])

def apply_mask(mask, val):
    masked = [choose_bit(entry) for entry in zip(mask, val)]
    return(''.join(masked))

def possibilities(masked, bit):
    if 'X' not in masked:
        return([masked])
    x = masked.index('X')
    if x == len(masked) - 1:
        new = ''.join([masked[:x], bit])
        return(possibilities(new, '0') + possibilities(new, '1'))
    else:
        new = ''.join([masked[:x], bit, masked[x+1:]])
        return(possibilities(new, '0') + possibilities(new, '1'))
    return([])


def all_possibilities(masked):
    return(list(set(possibilities(masked, '0') + possibilities(masked, '1'))))


def follow_instructions(input):
    m = {}
    mask = ''
    for line in input:
        if 'mask' in line:
            mask = line.split(" ")[-1]
        else:
            val = int(line.split(" ")[-1])
            loc = int((line.split("]")[0].split("[")[1]))
            loc = '{:036b}'.format(loc)
            masked = apply_mask(mask, loc)
            locs = [int(loc, 2) for loc in all_possibilities(masked)]
            for loc in locs:
                m[loc] = val
    return(sum(m.values()))
         

print(follow_instructions(entries))
