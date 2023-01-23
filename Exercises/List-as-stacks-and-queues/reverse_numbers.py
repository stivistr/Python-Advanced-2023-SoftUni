sequence_of_digits = list(input().split())

for i in range(len(sequence_of_digits)):
    print(sequence_of_digits.pop(), end=' ')

