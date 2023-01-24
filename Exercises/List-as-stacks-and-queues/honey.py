from collections import deque

bees = deque(int(x) for x in input().split())
nectars = deque(int(x) for x in input().split())
symbols = deque(input().split())

honey = 0

operations = {
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
}

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if bee <= nectar:
        honey += abs(operations[symbols.popleft()](bee, nectar))
    else:
        bees.appendleft(bee)

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")