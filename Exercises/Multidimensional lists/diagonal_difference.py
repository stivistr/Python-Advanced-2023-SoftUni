n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]

primary_diagonal = []
secondary_diagonal = []

for r in range(len(matrix)):
    primary_diagonal.append(matrix[r][r])

for r in range(len(matrix)):
    secondary_diagonal.append(matrix[r][n - r - 1])

difference_of_diagonals = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(difference_of_diagonals)