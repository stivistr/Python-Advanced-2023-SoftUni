rows, cols = [int(num) for num in input().split()]

OPPONENTS_COUNT = 3
touched_opponents = 0
moves = 0

matrix = []
my_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(rows):
    line = input().split()
    matrix.append(line)

    if 'B' in line:
        my_pos = [row, line.index('B')]
        matrix[row][my_pos[1]] = '-'

while touched_opponents != 3:
    direction = input()

    if direction == 'Finish':
        break

    r = directions[direction][0] + my_pos[0]
    c = directions[direction][1] + my_pos[1]

    if not (0 < r < rows and 0 < c < cols):
        continue

    if matrix[r][c] == 'O':
        continue

    my_pos = [r, c]

    if matrix[r][c] == 'P':
        touched_opponents += 1
        matrix[r][c] = '-'
        moves += 1
    elif matrix[r][c] == '-':
        moves += 1

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves}")