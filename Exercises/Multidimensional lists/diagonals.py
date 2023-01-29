n = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(n)]

primary_diagonal = []
secondary_diagonal = []

for r in range(len(matrix)):
    primary_diagonal.append(matrix[r][r])

for r in range(len(matrix)):
    secondary_diagonal.append(matrix[r][n - r - 1])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
