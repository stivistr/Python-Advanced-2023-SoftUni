from collections import deque

kids = input().split(' ')
toss = int(input())
players_deque = deque(kids)

while len(players_deque) > 1:
    for _ in range(toss - 1):
        players_deque.append(players_deque.popleft())

    print(f"Removed {players_deque.popleft()}")

print(f'Last is {players_deque[0]}')