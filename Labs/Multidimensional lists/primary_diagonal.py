rows = int(input())

matrix = []

for _ in range(rows):
    current_row = [int(el) for el in input().split()]
    matrix.append(current_row)

primary_diagonal = 0

for i in range(len(matrix) - 1, -1, -1):
    primary_diagonal += matrix[i][rows - i - 1]

print(primary_diagonal)
