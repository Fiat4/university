import os
import random
from . import game, writer


def clear():
    os.system("cls")


def runner(lives, words) -> None:
    record = writer.get_record()
    print(f"Прошлый рекорд: {record}")
    guessed = 0

    while True:
        result = game(words.pop(random.randint(0, len(words) - 1)), lives)

        if result:
            guessed += 1

        if not words:
            print(
                "У меня кончились слова, поэтому я не буду вам даже предлагать сыграть повторно. Вы меня обыграли уже"
            )
            break

        if not input("Желаете ли сыграть ещё раз? [y/n]: ").lower() in ["y", "д"]:
            print("Очень жаль! До встречи")
            break

        clear()

    if guessed > record:
        writer.write_record(guessed)
        print(f"Вы отгадали {guessed} слов(а), установив новый рекорд")
    else:
        print(f"Вы отгадали {guessed} слов, но рекорд равен {record}")


def menu() -> None:

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

    words = writer.get_words()
    runner(lives, words)
