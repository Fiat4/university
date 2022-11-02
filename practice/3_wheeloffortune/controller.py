import os
import random
from . import game, writer


def clear():
    os.system("cls")
    
    
def runner(lives, words) -> None:
    record = 0
    while True:
        result = game(words.pop(random.randint(0, len(words) - 1)), lives)
        if not result:
            writer.check_and_write_record(record)
            record = 0
        else:
            record += 1
            
        print(f"Угадано подряд слов: {record}")
        
        if not words:
            print(
                "У меня кончились слова, поэтому я не буду вам даже предлагать сыграть повторно. Вы меня обыграли уже"
            )
            break

        if not input("Желаете ли сыграть ещё раз? [y/n]: ").lower() in ["y", "д"]:
            print("Очень жаль! До встречи")
            break
        clear()

    writer.check_and_write_record(record)


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
