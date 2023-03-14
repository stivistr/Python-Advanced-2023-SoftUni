from collections import deque

textiles = deque([int(el) for el in input().split()])
medicaments = deque([int(el) for el in input().split()])

created_items = {}

healing_items = {
    'Patch': 30,
    'Bandage': 40,
    'MedKit': 100,
}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    healing_value = textile + medicament

    for item, value in healing_items.items():
        if healing_value == value:
            if item in created_items:
                created_items[item] += 1
            else:
                created_items[item] = 1
            break

        elif healing_value > healing_items['MedKit']:
            if 'MedKit' in created_items.keys():
                created_items['MedKit'] += 1
            else:
                created_items['MedKit'] = 1

            remaining_resource = healing_value - 100
            medicament = medicaments.pop()
            medicament += remaining_resource
            medicaments.append(medicament)
            break

        if healing_value not in healing_items.values():
            medicament += 10
            medicaments.append(medicament)
            break

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

if created_items:
    created_items = sorted(created_items.items(), key=lambda x: (-x[1], x))

    for item in created_items:
        print(f"{item[0]} - {item[1]}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")

if medicaments:
    print(f"Medicaments left: {', '.join(map(str, sorted(medicaments, reverse=True)))}")