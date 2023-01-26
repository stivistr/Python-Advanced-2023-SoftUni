n, m = input().split()

first_set = set()
second_set = set()

for _ in range(int(n)):
    num = int(input())
    first_set.add(num)

for _ in range(int(m)):
    num = int(input())
    second_set.add(num)

unique_elements = first_set.intersection(second_set)

print(*unique_elements, sep='\n')

