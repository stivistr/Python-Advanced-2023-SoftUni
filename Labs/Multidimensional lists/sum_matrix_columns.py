rows, cols = list(map(int, input().split(', ')))

matrix = []

for _ in range(rows):
    current_row = [int(el) for el in input().split()]
    matrix.append(current_row)

rows = len(matrix)
cols = len(matrix[0])

for i in range(cols):
    col_sum = 0
    for j in range(rows):
        col_sum += matrix[j][i]

    print(col_sum)
