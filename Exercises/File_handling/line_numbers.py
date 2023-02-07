from string import punctuation

with open('text.txt', 'r') as file:

    lines_in_file = file.readlines()

new_file = open('output.txt', 'w')

for line in range(len(lines_in_file)):
    row = lines_in_file[line]
    letters_count = 0
    punc_marks_count = 0

    for idx in row:
        if idx.isalpha():
            letters_count += 1
        elif idx in punctuation:
            punc_marks_count += 1

    new_file.write(f"Line {line + 1}: {''.join(el for el in row[:-1])} ({letters_count})({punc_marks_count})\n")

new_file.close()

