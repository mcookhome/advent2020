
with open("input.txt", "r") as file:
    entries = [int(entry) for entry in file]
    entries = sorted(entries)

seen = {0:1}

def dp(start):
    if start in seen:
        return(seen[start])
    if start not in entries:
        return(0)
    if start < 0:
        return(seen[start]) 
    ways = sum([dp(start - 1), dp(start - 2), dp(start - 3)])
    seen[start] = ways
    return(ways)

print(dp(max(entries)))
