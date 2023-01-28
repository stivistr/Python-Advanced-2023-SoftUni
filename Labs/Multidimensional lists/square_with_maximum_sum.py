rows, cols = list(map(int, input().split(', ')))

matrix = []
submatrix = []
MAX_SUM = float('-inf')

for _ in range(rows):
    current_row = [int(el) for el in input().split(', ')]
    matrix.append(current_row)

for r in range(len(matrix) - 1):
    for c in range(len(matrix[r]) - 1):
        if matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1] > MAX_SUM:
            MAX_SUM = matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1]
            submatrix.clear()
            submatrix = [[matrix[r][c], matrix[r][c + 1]], [matrix[r + 1][c], matrix[r + 1][c + 1]]]

for row in range(len(submatrix)):
    print(*submatrix[row])

print(MAX_SUM)
