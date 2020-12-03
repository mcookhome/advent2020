data = []

with open("input.txt", "r") as file:
    for line in file:
        line = "".join(line.split(":"))
        line = "".join(line.split("\n"))
        print(line.split(" "))
        splitline = line.split(" ")
        entry = {}
                
        entry["high_index"] = int(splitline[0].split("-")[1]) 
        entry["low_index"] = int(splitline[0].split("-")[0]) 
        entry["target"] = splitline[1]
        entry["password"] = splitline[2]
        data.append(entry)

print(len(data))
        
def count_valid(pws):
    count = 0
    for entry in data:
        password = entry["password"]
        if (password[entry["low_index"] - 1] == entry["target"]) ^ (password[entry["high_index"] - 1] == entry["target"]):
            count = count + 1
    return(count)

print(count_valid(data))
