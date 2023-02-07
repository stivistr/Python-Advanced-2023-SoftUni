import os

while True:

    command = input()

    if command == "End":
        break

    command_name, *data = command.split('-')

    if command_name == 'Create':
        created_file = open(f'{data[0]}', 'w')
        created_file.close()

    elif command_name == 'Add':
        with open(f'{data[0]}', 'a') as doc:
            doc.write(f'{data[1]}\n')

    elif command_name == 'Replace':
        try:
            with open(f'{data[0]}', 'r') as doc:
                text = doc.readlines()

            for idx in range(len(text)):
                text[idx] = text[idx].replace(data[1], data[2])

        except FileNotFoundError:
            print("An error occurred")

    elif command_name == 'Delete':
        try:
            os.remove(data[0])
        except FileNotFoundError:
            print("An error occurred")
