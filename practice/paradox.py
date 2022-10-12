import random 
DAYS = 365

def birthday(iterations, count):

    paradoxed = 0
    ok = 0

    for _ in range(iterations):
        birthdays = [random.randint(1, DAYS) for _ in range(count)]
        unique = set(birthdays)
        if len(birthdays) != len(unique):
            paradoxed += 1
        else:
            ok += 1


    return  f"""Всего итераций:{iterations}
Парадокс произошел в : {paradoxed/iterations * 100}%
Всё интиутивно: {ok/iterations * 100}%"""

def get_opened_door(win_door: int, choice: int) -> int:
    for i in range(1, 4):
        if i != win_door and i != choice:
            return i


def switch(choice: int, doors:list[int]) -> int:
    doors.remove(choice)
    return doors[0]

def monty_hall(iterations):


    win_with_change = 0
    win_without_change = 0


    for _ in range(iterations):
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
            
    return f"""Всего дверей открыто:{iterations}
Шанс победы не меняя выбор: {win_without_change/iterations * 100}%
Выбор менялся: {win_with_change/iterations * 100}%"""