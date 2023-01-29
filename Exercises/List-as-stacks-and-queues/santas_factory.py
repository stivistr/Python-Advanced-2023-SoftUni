from collections import deque

line_of_materials = deque(int(el) for el in input().split())
magic_level = deque(int(el) for el in input().split())

crafted_presents = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

presents_costs = {
    'Doll': 150,
    'Wooden train': 250,
    'Teddy bear': 300,
    'Bicycle': 400,
}

while line_of_materials and magic_level:
    box_of_materials = line_of_materials.pop()
    magic = magic_level.popleft()

    if box_of_materials == 0 or magic == 0:
        continue

    searched_present = box_of_materials * magic

    for k, v in presents_costs.items():
        if searched_present == v:
            crafted_presents[k] += 1

    if searched_present < 0:
        searched_present = box_of_materials + magic
        line_of_materials.append(searched_present)

    elif searched_present not in presents_costs.values() and searched_present > 0:
        box_of_materials += 15
        line_of_materials.append(box_of_materials)

    if crafted_presents["Doll"] > 0 and crafted_presents["Wooden train"] > 0:
        print("The presents are crafted! Merry Christmas!")
        break
    elif crafted_presents["Teddy bear"] > 0 and crafted_presents["Bicycle"] > 0:
        print("The presents are crafted! Merry Christmas!")
        break


print("No presents this Christmas!")

if line_of_materials:
    print(f"Materials left: {', '.join(str(x) for x in line_of_materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for k, v in sorted(crafted_presents.items()):
    print(f"{k}: {v}\n")