from collections import deque

line_of_substrings = deque(input().split())

main_colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']

req_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

searched_colors = []

while line_of_substrings:
    first_substring = line_of_substrings.popleft()
    second_substring = line_of_substrings.pop() if line_of_substrings else ''

    for color in (first_substring + second_substring, second_substring + first_substring):
        if color in main_colors:
            searched_colors.append(color)
            break
    else:
        for el in (first_substring[:-1], second_substring[:-1]):
            if el:
                line_of_substrings.insert(len(line_of_substrings) // 2, el)

for color in set(req_colors.keys()).intersection(searched_colors):
    if not req_colors[color].issubset(searched_colors):
        searched_colors.remove(color)

print(searched_colors)



