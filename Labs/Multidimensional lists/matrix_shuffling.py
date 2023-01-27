def swap_func(matrices):
    while True:
        command, *info = [int(el) if el.isdigit() else el for el in input().split()]

        if command == 'END':
            break

        if command == 'swap' and len(info) == 4:
            r1, c1, r2, c2 = info
            if 0 <= r1 <= rows and 0 <= r2 <= rows and 0 <= c1 <= cols and 0 <= c2 <= cols:
                matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
                [print(*row) for row in matrix]
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")


rows, cols = [int(el) for el in input().split()]

matrix = [[int(el) if el.isdigit() else el for el in input().split()] for _ in range(rows)]
matrix_shuffle = swap_func(matrix)
