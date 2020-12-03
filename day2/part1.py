data = []

with open("input.txt", "r") as file:
    for line in file:
        line = "".join(line.split(":"))
        line = "".join(line.split("\n"))
        print(line.split(" "))
        splitline = line.split(" ")
        entry = {}
                
        entry["max_freq"] = int(splitline[0].split("-")[1]) 
        entry["min_freq"] = int(splitline[0].split("-")[0]) 
        entry["target"] = splitline[1]
        entry["password"] = splitline[2]
        data.append(entry)

print(len(data))
        
def count_valid(pws):
    count = 0
    for entry in data:
        freq = entry["password"].count(entry["target"])
        if entry["min_freq"] <= freq and entry["max_freq"] >= freq:
            count = count + 1
    return(count)

print(count_valid(data))
