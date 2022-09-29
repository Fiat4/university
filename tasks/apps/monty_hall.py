import random

COUNT = 1000000

win_with_change = 0
win_without_change = 0
total = 0

while total < COUNT:
    total += 1
    doors = [1, 2, 3]
    win_door = random.randint(1, 3)
    doors.remove(win_door)
    choice = random.randint(1, 3)
    if choice != win_door:
        doors.remove(choice)
    opened_door = random.choice(doors)
    result_doors = [1, 2, 3]
    result_doors.remove(opened_door)

    if win_door == choice:
        win_without_change += 1
    else:
        win_with_change += 1

print(
    f"""Всего дверей открыто:{total}
Шанс победы не меняя выбор: {win_without_change/total * 100}%
Выбор менялся: {win_with_change/total * 100}%"""
)
