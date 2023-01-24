first_seq = set(int(x) for x in input().split())
second_seq = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_command, *data = input().split()

    command = first_command + ' ' + data.pop(0)

    if command == 'Add First':
        [first_seq.add(int(el)) for el in data]
    elif command == 'Add Second':
        [second_seq.add(int(el)) for el in data]
    elif command == 'Remove First':
        [first_seq.discard(int(el)) for el in data]
    elif command == 'Remove Second':
        [second_seq.discard(int(el)) for el in data]
    else:
        if first_seq.issubset(second_seq) or second_seq.issubset(first_seq):
            print(True)
        else:
            print(False)

print(*first_seq, sep=', ')
print(*second_seq, sep=', ')