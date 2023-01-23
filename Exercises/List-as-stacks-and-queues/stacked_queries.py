stack = []

for n in range(int(input())):

    numbers = input().split()

    if numbers[0] == '1':
        stack.append(int(numbers[1]))
    elif numbers[0] == '2':
        if stack:
            stack.pop()
    elif numbers[0] == '3':
        if stack:
            print(max(stack))
    elif numbers[0] == '4':
        if stack:
            print(min(stack))

if stack:
    stack.reverse()
    print(*stack, sep=", ")
else:
    print(None)

