matrix = [list(map(int, input().split())) for _ in range(int(input()))]

while True:
    command = input()

    if command == 'END':
        break

    command_name, *indexes = command.split()

    if command_name == 'Add':
        curr_row = int(indexes[0])
        curr_col = int(indexes[1])
        value = int(indexes[2])

        if curr_row in range(0, len(matrix)) and curr_col in range(0, len(matrix)):
            matrix[curr_row][curr_col] += value
        else:
            print("Invalid coordinates")

    elif command_name == 'Subtract':
        curr_row = int(indexes[0])
        curr_col = int(indexes[1])
        value = int(indexes[2])

        if curr_row in range(0, len(matrix)) and curr_col in range(0, len(matrix)):
            matrix[curr_row][curr_col] -= value
        else:
            print("Invalid coordinates")

[print(*row) for row in matrix]