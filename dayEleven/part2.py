import copy

def find_seat(poss, delta, seats):
    if not validate_neighbor(poss, seats):
        return(poss)
    elif seats[poss[0]][poss[1]] == '.':
        return(find_seat((poss[0] + delta[0], poss[1] + delta[1]), delta, seats))
    else:
        return(poss)


def neighbors(row, col, seats):
    all_poss = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)] 
    all_poss = [find_seat((row + poss[0], col + poss[1]), poss, seats) for poss in all_poss]
    all_poss = [poss for poss in all_poss if validate_neighbor(poss, seats)]
    return(all_poss)

def validate_neighbor(poss, seats):
    val = poss[0] >= 0 and poss[1] >= 0 and poss[0] < len(seats) and poss[1] < len(seats[0])
    return val


with open("input.txt", "r") as file:
    entries = [list(entry.strip()) for entry in file]

def num_person(seat):
    if seat == '#':
        return(1)
    return(0)


def one_iteration(seats):
    new = copy.deepcopy(seats)
    changed = False
    for i in range(len(entries)):
        for j in range(len(entries[0])):
            all_poss = neighbors(i,j,seats)
            vals = [seats[poss[0]][poss[1]] for poss in all_poss]
            people = [num_person(seat) for seat in vals] 
            if seats[i][j] == '#' and sum(people) >= 5:
                changed = True
                new[i][j] = 'L'
            elif seats[i][j] == 'L' and sum(people) == 0:
                changed = True
                new[i][j] = '#'
            else:
                new[i][j] = seats[i][j]
    return((new, changed))


def life(seats):
    iteration = 0
    while True:
        result = one_iteration(seats)
        iteration = iteration + 1
        print(iteration)
        seats = result[0]
        if not result[1]:
            print("Seats are filled! number of people boarded:")
            people = [sum([num_person(seat) for seat in row]) for row in seats]
            return(sum(people))

print(life(entries)) 
