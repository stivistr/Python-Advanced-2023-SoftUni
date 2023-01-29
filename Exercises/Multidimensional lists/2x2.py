rows, cols = list(map(int, input().split()))

matrix = [[el for el in input().split()] for _ in range(rows)]

square_matrices = 0

for r in range(len(matrix) - 1):
    for c in range(cols - 1):
        if matrix[r][c] == matrix[r][c + 1] \
                and matrix[r][c] == matrix[r + 1][c] \
                and matrix[r][c] == matrix[r + 1][c + 1]:
            square_matrices += 1

print(square_matrices)