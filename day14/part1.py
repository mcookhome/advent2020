
with open("input.txt", "r") as file:
    entries = [entry.strip() for entry in file]

def choose_bit(pair):
    if pair[0] == 'X':
        return(pair[0])
    else:
        return(pair[1])



def apply_mask(mask, val):
    masked = [choose_bit(entry) for entry in zip(mask, val)]
    return(''.join(masked))

mask = '000000000000000000000000000000X1001X'
val = '{:036b}'.format(42)
print(apply_mask(mask, val))

def follow_instructions(input):
    m = {}
    mask = ''
    for line in input:
        if 'mask' in line:
            mask = line.split(" ")[-1]
        else:
            val = int(line.split(" ")[-1])
            loc = (line.split("]")[0].split("[")[1])
            val = '{:036b}'.format(val)
            masked = apply_mask(mask, val)
            m[loc] = masked
    return(sum([int(val, 2) for val in m.values()]))
         

print(follow_instructions(entries))

