data = []

with open("input.txt", "r") as file:
    for line in file:
        data.append(list(line[:-1]))
    print(len(data))
    print(len(data[0]))

        
def count_trees(rows, x, y):
    row = 0
    col = 0
    width = len(rows[0])
    trees = 0
    while row < len(rows) - y:
        row = row + y
        col = col + x
        #print(row)
        #print(col % width)
        if data[row][col % width] == '#':
            trees = trees + 1
    return(trees)


print(count_trees(data, 1, 1))
print(count_trees(data, 3, 1))
print(count_trees(data, 5, 1))
print(count_trees(data, 7, 1))
print(count_trees(data, 1, 2))

