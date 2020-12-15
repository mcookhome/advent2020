f = [0,13,1,8,6,15]

def ins(d, key, count):
    if key in d:
        d[key] = (d[key][1], count)
    else:
        d[key] = (-1, count)

def play_game(start, iteration):
    seen = {}
    most_recent = 0
    count = 0
    for num in start:
        count = count + 1
        ins(seen, num, count)
        most_recent = num
    while count < iteration:
        count = count + 1
        if most_recent in seen:
            if seen[most_recent][0] == -1:
                 most_recent = 0
                 ins(seen, most_recent, count)
            else:
                 most_recent = seen[most_recent][1] - seen[most_recent][0]
                 ins(seen, most_recent, count)
        else:
            most_recent = 0
            ins(seen, most_recent, count)
    return((count, most_recent))

print(play_game(f, 2020))
print(play_game(f, 30000000))
