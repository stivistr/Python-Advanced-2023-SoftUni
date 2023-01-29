rows, cols = list(map(int, input().split()))

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

MAX_SUM = float('-inf')
square_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = matrix[row][col:col + 3]
        second_row = matrix[row + 1][col:col + 3]
        third_row = matrix[row + 2][col:col + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > MAX_SUM:
            MAX_SUM = current_sum
            square_matrix = [first_row, second_row, third_row]

print(f"Sum = {MAX_SUM}")
[print(*square_matrix[row]) for row in range(3)]