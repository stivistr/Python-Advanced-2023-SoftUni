box_of_clothes = list(int(x) for x in input().split())
capacity_of_rack = int(input())
current_capacity = capacity_of_rack
count_of_racks = 1

while box_of_clothes:

    current_cloth = box_of_clothes.pop()

    if current_capacity - current_cloth >= 0:
        current_capacity -= current_cloth
    else:
        count_of_racks += 1
        current_capacity = capacity_of_rack - current_cloth

print(count_of_racks)

