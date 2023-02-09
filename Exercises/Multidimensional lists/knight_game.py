size = int(input())
board = [[el for el in input()] for _ in range(size)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, -1),
    (1, -2),
    (2, 1),
    (1, 2),
)

removed_knights = 0

while True:
    max_attacks = 0
    knights_with_max_attacks = []

    for row in range(size):
        for col in range(size):
            if board[row][col] == 'K':
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if board[pos_row][pos_col] == 'K':
                            attacks += 1

                if attacks > max_attacks:
                    knights_with_max_attacks = [row, col]
                    max_attacks = attacks

    if max_attacks:
        r, c = knights_with_max_attacks
        board[r][c] = '0'
        removed_knights += 1
    else:
        break

print(removed_knights)