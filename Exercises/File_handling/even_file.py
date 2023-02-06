symbols = ["-", ",", ".", "!", "?"]

with open("text.txt", "r") as even_lines:
    file = even_lines.readlines()

for row in range(0, len(file), 2):

    for symbol in symbols:
        file[row] = file[row].replace(symbol, "@")

    print(*file[row].split()[::-1], sep=' ')
