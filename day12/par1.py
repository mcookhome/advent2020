dirs = { 0: 'E', 90: 'S', 180: 'W', 270: 'N' }

with open("input.txt", "r") as file:
    entries = [entry.strip() for entry in file]
    entries = [(entry[0], int(entry[1:])) for entry in entries]


def eval_instructions(moves):
    dir = 0
    x = 0
    y = 0
    for move in moves:
        c = move[0]
        val = move[1]
        if c == 'R':
            dir = (dir + val) % 360
        if c == 'L':
            dir = (dir - val) % 360
        if c == 'F':
            c = dirs[dir]
        if c == 'W':
            x = x - val
        if c == 'E':
            x = x + val
        if c == 'N':
            y = y + val
        if c == 'S':
            y = y - val
    return(abs(x) + abs(y))         

print(eval_instructions(entries))
