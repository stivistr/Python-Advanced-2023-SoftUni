def print_func(parking_data):
    if parking_data:
        for car in parking_data:
            print(car)
    else:
        print("Parking Lot is Empty")


n = int(input())
parking_lot = set()

for _ in range(n):

    direction, plate = input().split(', ')

    if direction == 'IN':
        parking_lot.add(plate)
    elif direction == 'OUT':
        parking_lot.remove(plate)

print_func(parking_lot)
