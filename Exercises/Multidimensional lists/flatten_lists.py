elements = [el for el in input().split('|')]
digits = []

for el in range(len(elements) - 1, -1, -1):
    digits.extend(elements[el].split())

print(*digits)