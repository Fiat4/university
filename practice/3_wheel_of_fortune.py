import os
import random

SQUARE = "\u25A0"
words = ["книга", "слово"]


def clear():
    os.system("cls")


def game(word: str, lives: int) -> None:
    size = len(word)
    frame = [SQUARE for _ in range(size)]
    while lives > 0:
        print(f"{''.join(frame)} | ❤x{lives}")
        guess = input("Введите букву или слово целиком: ").lower()
        if guess == word:
            print("Вы победили! Приз в студию!")
            break
        if len(guess) != 1:
            print("Вы ошиблись! Я забираю у вас 1 жизнь")
            lives -= 1
            continue
        idxs = [index for index in range(size) if guess == word[index]]
        if not idxs:
            print("Такой буквы нет! Я забираю у вас 1 жизнь")
            lives -= 1
            continue
        for idx in idxs:
            frame[idx] = guess

        if SQUARE not in frame:
            print("Вы победили! Приз в студию!")
            break

clear()
print("Добро пожаловать на поле чудес!")
print("В игре несколько уровней сложности:")
print("[1] Новичок")
print("[2] Уже смешарик")
print("[3] Я легенда")

match input("Выберите: "):
    case "1":
        lives = 7
    case "2":
        lives = 5
    case "3":
        lives = 3
    case _:
        print(
            "Обманом не разбогатеешь, а обеднеешь. Получи-ка одну жизнь. У тебя нет права на ошибку"
        )
        lives = 1

while True:
    game(words.pop(random.randint(0, len(words) - 1)), lives)
    if not words:
        print(
            "У меня кончились слова, поэтому я не буду вам даже предлагать сыграть повторно. Вы меня обыграли уже"
        )
        break
    if not input("Желаете ли сыграть ещё раз? [y/n]: ").lower() in ["y", "д"]:
        print("Очень жаль! До встречи")
        break
    clear()
