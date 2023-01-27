number_of_rows = int(input())

matrix = []

for _ in range(number_of_rows):
    current_row = [int(el) for el in input().split(', ')]
    matrix.append(current_row)

result = [num for row in matrix for num in row]
print(result)
