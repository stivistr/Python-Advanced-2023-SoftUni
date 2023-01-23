from collections import deque

pumps_queue = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pumps_queue_copy = pumps_queue.copy()
liters_in_tank = 0
index = 0

while pumps_queue_copy:
    petrol, distance = pumps_queue_copy.popleft()

    liters_in_tank += petrol

    if liters_in_tank - distance < 0:
        pumps_queue.rotate(-1)
        pumps_queue_copy = pumps_queue.copy()
        index += 1
        liters_in_tank = 0
    else:
        liters_in_tank -= distance

print(index)
