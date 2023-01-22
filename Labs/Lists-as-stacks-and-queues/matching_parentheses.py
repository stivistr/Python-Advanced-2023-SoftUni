expression = input()
parentheses = []

for i in range(len(expression)):
    ch = expression[i]

    if ch == '(':
        parentheses.append(i)
    elif ch == ')':
        last_opening = parentheses.pop()
        searched_set = expression[last_opening:i + 1]
        print(searched_set)
