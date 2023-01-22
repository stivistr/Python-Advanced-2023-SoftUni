supermarket = []
COMMAND_END = 'End'
COMMAND_PAID = 'Paid'

while True:
    command = input()

    if command == COMMAND_PAID:
        for i in range(len(supermarket)):
            print(supermarket.pop(0))

    elif command == COMMAND_END:
        print(f'{len(supermarket)} people remaining.')
        break

    else:
        supermarket.append(command)

