from collections import deque


def add_names_in_deque():
    people = deque()

    while True:
        name = input()

        if name == COMMAND_Start:
            break
        people.append(name)

    return people


water_amount = int(input())
COMMAND_END = 'End'
COMMAND_Start = 'Start'
people_deque = add_names_in_deque()

while True:
    command = input().split(' ')

    if command[0] == COMMAND_END:
        print(f"{water_amount} liters left")
        break
    elif command[0] == 'refill':
        water_amount += int(command[1])
    else:
        person = people_deque.popleft()
        current_litres = int(command[0])

        if current_litres <= water_amount:
            print(f"{person} got water")
            water_amount -= current_litres
        else:
            print(f"{person} must wait")