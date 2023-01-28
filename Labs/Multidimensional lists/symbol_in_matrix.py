rows = int(input())

matrix = []

for _ in range(rows):
    current_row = [el for el in input()]
    matrix.append(current_row)

symbol = input()
symbol_idx = []

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == symbol:
            symbol_idx.append(r)
            symbol_idx.append(c)
            break

if symbol_idx:
    print(f"({symbol_idx[0]}, {symbol_idx[-1]})")
else:
    print(f"{symbol} does not occur in the matrix")
