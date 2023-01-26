n = int(input())

set_of_elements = set()

for row in range(n):
    elements = input().split()
    for el in range(len(elements)):
        set_of_elements.add(elements[el])

print(*set_of_elements, sep='\n')