def collect_data_for_arrived_guests():
    guests_arrived = []
    while True:
        guest = input()

        if guest == 'END':
            break
        else:
            guests_arrived.append(guest)

    return guests_arrived


def print_func(missing_guests):
    print(len(missing_guests))
    for person in sorted(missing_guests):
        print(person)


n = int(input())

guest_reservation_list = [input() for _ in range(n)]
arrived_guests = collect_data_for_arrived_guests()
guests_missing = set(guest_reservation_list).difference(arrived_guests)
print_func(guests_missing)