
with open("input.txt", "r") as file:
    entries = [entry.split("\n") for entry in file.read().split("\n\n")]
    sets = [''.join(set(''.join(entry))) for entry in entries]
    print(sum([len(set) for set in sets]))
