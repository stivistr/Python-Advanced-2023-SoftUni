from collections import deque

quantity_of_food = int(input())
queue = deque(int(x) for x in input().split())

print(max(queue))

for order in queue.copy():

    if quantity_of_food - order >= 0:
        quantity_of_food -= order
        queue.popleft()
    else:
        print(f"Orders left: {' '.join(str(x) for x in queue)}")
        break
else:
    print("Orders complete")
