from collections import deque

line_of_materials = deque(int(el) for el in input().split())
magic_level = deque(int(el) for el in input().split())

crafted_presents = []

presents_costs = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while line_of_materials and magic_level:
    box_of_materials = line_of_materials.pop() if magic_level[0] or not line_of_materials[0] else 0
    magic = magic_level.popleft() if box_of_materials or not magic_level[0] else 0

    if not magic:
        continue

    searched_present = box_of_materials * magic

    if presents_costs.get(searched_present):
        crafted_presents.append(presents_costs[searched_present])
    elif searched_present < 0:
        line_of_materials.append(box_of_materials + magic)
    elif searched_present > 0:
        line_of_materials.append(box_of_materials + 15)

if {"Doll", "Wooden train"}.issubset(crafted_presents) or {"Teddy bear", "Bicycle"}.issubset(crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if line_of_materials:
    print(f"Materials left: {', '.join([str(x) for x in line_of_materials][::-1])}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

[print(f"{toy}: {crafted_presents.count(toy)}") for toy in sorted(set(crafted_presents))]

