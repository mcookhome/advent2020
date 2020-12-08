with open("input.txt", "r") as file:
    entries = [entry.strip().split(" ") for entry in file]
    entries = [(entry[0], int(entry[1])) for entry in entries]
    print(entries)

def program(input):
    visited = []
    index = 0
    acc = 0
    while True:
        if index == len(input):
            return((index, acc))
        if index in visited:
            return((index, acc))
            break
        visited.append(index)
        entry = input[index]
        if entry[0] == 'acc':
            acc = acc + entry[1]
            index = index + 1
        elif entry[0] == 'nop':
            index = index + 1
        elif entry[0] == 'jmp':
            index = index + entry[1]
                     
print(program(entries))

def replace_commands(input):
    target = len(input)
    for i in range(target):
        if input[i][0] == 'nop':
            copy = [cmd for cmd in input]
            copy[i] = ('jmp', input[i][1])
            result = program(copy)
            if result[0] == target:
                print(input[i])
                return(result)
        elif input[i][0] == 'jmp':
            copy = [cmd for cmd in input]
            copy[i] = ('nop', input[i][1])
            result = program(copy)
            if result[0] == target:
                print(input[i])
                return(result)
                     
print(replace_commands(entries))
