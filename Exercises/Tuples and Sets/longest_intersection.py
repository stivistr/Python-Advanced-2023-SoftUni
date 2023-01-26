longest_intersection = set()

for _ in range(int(input())):
    first_inter, second_inter = [el.split(',') for el in input().split('-')]

    first_range = set(range(int(first_inter[0]), int(first_inter[1]) + 1))
    second_range = set(range(int(second_inter[0]), int(second_inter[1]) + 1))

    intersection = first_range.intersection(second_range)

    if len(longest_intersection) < len(intersection):
        longest_intersection = intersection

print(f"Longest intersection is "
      f"[{', '.join([str(x) for x in longest_intersection])}]"
      f" with length {len(longest_intersection)}"
)