rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for row in range(rows):
    row_data = list(map(int, input().split(', ')))
    matrix.append(row_data)

sum_of_matrix = 0

for i in range(len(matrix)):
    current_row = matrix[i]
    sum_of_matrix += sum(current_row)

print(sum_of_matrix)
print(matrix)