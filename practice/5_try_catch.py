def open_file(filename: str):
    opened = False
    try:
        file = open(filename, "r")
        opened = True
        count = int(file.readline())

        return [int(x) for x in [file.readline() for _ in range(count)]]

    except FileNotFoundError:
        print("Такого файла нет, повторите попытку!")

    except ValueError:
        print(f"В файле есть не только числа!")

    except Exception as e:
        print(f"Неопознанная ошибка! {type(e)}, {e=}")

    finally:
        if opened:
            file.close()


while filename := input("Введите название файла: "):
    if result := open_file(filename):
        print(result)
        break
