text = input()

occurrences = {}

for el in text:
    if el not in occurrences:
        occurrences[el] = 0
    occurrences[el] += 1

for k,v in sorted(occurrences.items()):
    print(f"{k}: {v} time/s")