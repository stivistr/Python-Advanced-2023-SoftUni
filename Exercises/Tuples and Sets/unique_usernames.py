n = int(input())

unique_names = set()

for x in range(n):
    name = input()
    unique_names.add(name)

print(*unique_names, sep="\n")