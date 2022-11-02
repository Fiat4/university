import os
import random
from . import writer

SQUARE = "\u25A0"


def game(word: str, lives: int) -> bool:
    size = len(word)
    frame = [SQUARE for _ in range(size)]

    while lives > 0:
        print(f"{''.join(frame)} | ❤x{lives}")
        guess = input("Введите букву или слово целиком: ").upper()
        if guess == word.upper():
            print("Вы победили! Приз в студию!")
            return True
        if len(guess) != 1:
            print("Вы ошиблись! Я забираю у вас 1 жизнь")
            lives -= 1
            continue
        idxs = [index for index in range(size) if guess.lower() == word[index]]
        if not idxs:
            print("Такой буквы нет! Я забираю у вас 1 жизнь")
            lives -= 1
            continue

        for idx in idxs:
            frame[idx] = guess

        if SQUARE not in frame:
            print("Вы победили! Приз в студию!")
            return True

    return False
