from collections import deque

food_portions = deque(map(int, input().split(', ')))
stamina = deque(map(int, input().split(', ')))

mountain_peaks = {'Vihren': 80, 'Kutelo': 90, 'Banski Suhodol': 100, 'Polezhan': 60, 'Kamenitza': 70}
conquered_peaks = []

while food_portions and stamina:
    daily_food = food_portions.pop()
    daily_stamina = stamina.popleft()
    daily_try = daily_food + daily_stamina

    for peak, difficulty in mountain_peaks.items():
        if daily_try >= difficulty:
            conquered_peaks.append(peak)
            mountain_peaks.pop(peak)

        break

    if len(conquered_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break

if len(conquered_peaks) < 5:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    for peak in conquered_peaks:
        print(peak)


