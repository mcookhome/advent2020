def op(o, v1, v2):
    if o == '*':
        return(v1 * v2)
    if o == '+':
        return(v1 + v2)

def eval(entry):
    val = 0
    operator = '+'
    offset = 0
    for i in range(len(entry)):
        if i + offset >= len(entry):
            return(val)
        char = entry[i + offset]
        if char == '(':
            sub = eval(entry[i+offset+1:]) 
            val = op(operator, val, sub[0])
            offset = offset + sub[1]
        elif char == ')':
            return((val, i + offset + 1))
        elif char == ' ':
            continue
        elif char in '*+':
            operator = char
        else:
            val = op(operator, val, int(char))
    return(val)

with open("input.txt", "r") as file:
    entries = [entry.strip() for entry in file]
    print(sum([eval(entry) for entry in entries]))
