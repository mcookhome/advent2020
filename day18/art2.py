def op(o, v1, v2):
    if o == '*':
        return(v1 * v2)
    if o == '+':
        return(v1 + v2)

def last_exp(total, i):
    count = 0
    seen_paren = False
    while i >= 0:
        char = total[i]
        if char == ')':
            count = count + 1
            seen_paren = True
        if char == '(':
            count = count - 1
        if char.isdigit() and count == 0:
            return(i)
        if seen_paren and count == 0:
            return(i)
        i = i - 1
    return(i)

def next_exp(total, i):
    count = 0
    seen_paren = False
    while i <= len(total) - 1:
        char = total[i]
        if char == '(':
            count = count + 1
            seen_paren = True
        if char == ')':
            count = count - 1
        if char.isdigit() and count == 0:
            return(i)
        if seen_paren and count == 0:
            return(i)
        i = i + 1
    return(i)

def add_parentheses(entry):
    i = 0
    while i < len(entry) - 1:
        char = entry[i]
        if char == '+':
            l = last_exp(entry, i)
            entry = entry[:l] + '(' + entry[l:]
            r = next_exp(entry, i)
            entry = entry[:r+1] + ')' + entry[r+1:]
            i = i + 1 
        i = i + 1 
    return(entry)

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
    print(sum([eval(add_parentheses(entry)) for entry in entries]))
