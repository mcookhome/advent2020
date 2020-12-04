import re

data = []

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] 
def process_raw_entry(raw_entry):
    kvs = raw_entry.split()
    entry = {}
    for kv in kvs:
        pair = kv.split(":")
        entry[pair[0]] = pair[1]
    return(entry)


def is_valid_passport(passport):
    return(all([field in passport for field in fields]))  
     
final_entries = []


def valid_byr(i):
    return(len(i) == 4 and int(i)>=1920 and int(i)<=2002)

def valid_iyr(i):
    return(len(i) == 4 and int(i)>=2010 and int(i)<=2020)

def valid_eyr(i):
    return(len(i) == 4 and int(i)>=2020 and int(i)<=2030)

def valid_hgt(i):
    return(bool(re.match("(^1[5-8]\dcm$)|(^19[0-3]cm$)|59in$|(6[0-9])in$|(7[0-6])in$", i)))

print(valid_hgt("76cm"))
print(valid_hgt("70in"))

def valid_hcl(i):
    return(bool(re.match("^#([0-9]|[a-f]){6}$", i)))

def valid_ecl(i):
    return(bool(re.match("^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$", i)))

def valid_pid(i):
    return(bool(re.match("^\d{9}$", i)))

def valid_fields(passport):
    return(all([valid_byr(passport["byr"]),valid_iyr(passport["iyr"]),valid_eyr(passport["eyr"]),valid_hgt(passport["hgt"]),valid_ecl(passport["ecl"]),valid_hcl(passport["hcl"]),valid_pid(passport["pid"])]))

with open("input.txt", "r") as file:
    entries = [" ".join(entry.split("\n")) for entry in file.read().split("\n\n")]
    for raw in entries:
         entry = process_raw_entry(raw)
         data.append(entry)
    final_entries = [passport for passport in data if is_valid_passport(passport)]
    print(sum([is_valid_passport(passport) for passport in data]))
    print(sum([valid_fields(passport) for passport in final_entries]))

