numbers = tuple(map(float, input().split()))
counter_of_values = {}

for number in numbers:
    if number not in counter_of_values:
        counter_of_values[number] = 0
    counter_of_values[number] += 1

for k, v in counter_of_values.items():
    print(f"{k} - {v} times")