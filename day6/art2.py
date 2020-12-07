
with open("input.txt", "r") as file:
    entries = [[set(response) for response in entry.split("\n")] for entry in file.read().split("\n\n")]
    entries[-1] = entries[-1][:-1]
    print(entries)
    intersections = [set.intersection(*s) for s in entries]
    print(intersections)
    for i in range(len(entries)):
        print(str(entries[i]) + "," + str(intersections[i]))
    print(sum([len(i) for i in intersections]))

