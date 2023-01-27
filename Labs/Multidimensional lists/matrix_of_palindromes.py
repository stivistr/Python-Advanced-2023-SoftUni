rows, cols = list(map(int, input().split()))

start_end = ord('a')

for r in range(start_end, start_end + rows):
    for c in range(start_end, start_end + cols):
        print(f"{chr(r)}{chr((r + c - start_end))}{chr(r)}", end=' ')

    print()