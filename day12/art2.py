dirs = { 0: 'E', 90: 'S', 180: 'W', 270: 'N' }

with open("input.txt", "r") as file:
    entries = [entry.strip() for entry in file]
    entries = [(entry[0], int(entry[1:])) for entry in entries]

def counter90(pos):
    return((-pos[1], pos[0]))

def clock90(pos):
    return((pos[1], -pos[0]))

def eval_instructions(moves):
    dir = 0
    x = 0
    y = 0
    w = (10, 1)
    for move in moves:
        c = move[0]
        val = move[1]
        if c == 'R':
            while val > 0:
                w = clock90(w)
                val = val - 90
        if c == 'L':
            while val > 0:
                w = counter90(w)
                val = val - 90
        if c == 'F':
            x = x + (val * w[0])
            y = y + (val * w[1])
        if c == 'W':
            w = (w[0] - val, w[1])
        if c == 'E':
            w = (w[0] + val, w[1])
        if c == 'N':
            w = (w[0], w[1] + val)
        if c == 'S':
            w = (w[0], w[1] - val)
    return(abs(x) + abs(y))         

print(eval_instructions(entries))
