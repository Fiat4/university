import random

COUNT = 10000

win_with_change = 0
win_without_change = 0
total = 0


def get_opened_door(win_door: int, choice: int) -> int:
    for i in range(1, 4):
        if i != win_door and i != choice:
            return i


def switch(choice: int, doors: list[int]) -> int:
    doors.remove(choice)
    return doors[0]


while total < COUNT:
    total += 1
    doors = [1, 2, 3]
    win_door = random.randint(1, 3)
    choice = random.randint(1, 3)
    opened_door = get_opened_door(win_door, choice)
    doors.remove(opened_door)
    if win_door == choice:
        win_without_change += 1
    else:
        choice = switch(choice, doors)
        if choice == win_door:
            win_with_change += 1

print(
    f"""Всего дверей открыто:{total}
Шанс победы не меняя выбор: {win_without_change/total * 100}%
Выбор менялся: {win_with_change/total * 100}%"""
)
