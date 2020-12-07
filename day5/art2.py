
with open("input.txt", "r") as file:
    entries = [entry.strip() for entry in file]
    binary_seats = [(row[:7].replace("B", "1").replace("F", "0"), row[7:].replace("R", "1").replace("L", "0")) for row in entries]
    seats = [(int(seat[0], 2), int(seat[1], 2)) for seat in binary_seats]
    seat_ids = [8*seat[0]+seat[1] for seat in seats] 
    print(max(seat_ids))
    print(len(seat_ids))
    print(set(range(len(seat_ids))).difference(set(seat_ids)))
