
with open("input.txt", "r") as file:
    entries = [entry.strip() for entry in file]
    earliest = int(entries[0])
    routes = [int(entry) for entry in entries[1].split(",") if entry != 'x']
    wait_times = [(route, route * (earliest // route + 1) - earliest) for route in routes]
    wait_time = min(wait_times, key = lambda k: k[1])
    print(wait_time[0]*wait_time[1])
    
