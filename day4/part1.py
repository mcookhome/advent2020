data = []

def process_raw_entry(raw_entry):
    kvs = raw_entry.split()
    entry = {}
    for kv in kvs:
        pair = kv.split(":")
        entry[pair[0]] = pair[1]
    return(entry)


def is_valid_passport(passport):
    return(all([field in passport for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]]))  
     
with open("input.txt", "r") as file:
    entries = [" ".join(entry.split("\n")) for entry in file.read().split("\n\n")]
    for raw in entries:
         entry = process_raw_entry(raw)
         data.append(entry)
         
    print(entries)
    print(data)
    print([is_valid_passport(passport) for passport in data])
    print(sum([is_valid_passport(passport) for passport in data]))
