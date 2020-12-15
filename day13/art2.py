
from functools import reduce

with open("input.txt", "r") as file:
    entries = [entry.strip() for entry in file]
    routes = entries[1].split(",")
    routes = [(int(routes[i]), i) for i in range(len(routes)) if routes[i] != 'x']

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

route_nums = [route[0] for route in routes]
route_delays = [route[0] - route[1] for route in routes]

print(chinese_remainder(route_nums, route_delays))
