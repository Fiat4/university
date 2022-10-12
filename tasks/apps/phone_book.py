import os
import time


def clear() -> None:
    os.system("cls")


def normalize_name(name: str) -> str:
    return " ".join([x.capitalize() for x in name.split()])


def normalize_phone(phone: str) -> str:
    clean = "".join(filter(str.isdigit, phone))

    if len(clean) == 10:
        return f"+7{clean}"
    elif len(clean) == 11 and clean[0] in ["8", "7"]:
        return f"+7{clean[1:]}"
    else:
        # Номер, вероятно, не российский
        return clean


def add_contact(phone_book: dict[str, str]) -> bool:
    phone = normalize_phone(input("Введите телефон: "))
    name = normalize_name(input("Введите имя: "))
    phone_book.update({name: phone})
    return True


def remove_contact(phone_book: dict[str, str]) -> bool:
    name = normalize_name(input("Введите имя: "))
    return bool(phone_book.pop(name, 0))


def modify_contact(phone_book: dict[str, str]) -> bool:
    name = normalize_name(input("Введите имя контакта: "))
    if not phone_book.get(name, 0):
        print("Контакт не найден")
        return False
    phone = normalize_phone(input("Введите телефон: "))
    phone_book[name] = phone
    return True


def list_contacts(phone_book: dict[str, str]) -> None:
    if len(phone_book.keys()) == 0:
        return print("Книжка пуста")

    name = input(
        "Введите имя для поиска по имени или Enter для вывода всех контактов: "
    )

    if not name:
        for k, v in phone_book.items():
            print(k, v)
    else:
        print(phone_book.get(normalize_name(name), "Такого контакта нет"))


def menu() -> None:
    phone_book: dict[str, str] = {}

    while True:
        clear()
        print("Доступные действия:")
        print("[1] Добавить контакт")
        print("[2] Удалить контакт (по имени)")
        print("[3] Показать контакт(ы)")
        print("[4] Изменить номер телефона (по имени)")
        print("[0] Выйти")

        action = int(input("Выбор: "))

        match action:
            case 1:
                add_contact(phone_book)
            case 2:
                remove_contact(phone_book)
            case 3:
                list_contacts(phone_book)
            case 4:
                modify_contact(phone_book)
            case 0:
                return
            case _:
                print("Некорректный ввод. Повторите...")

        input("\nНажмите кнопку для возврата в меню...")


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        clear()
        print("Работа с книжкой завершена. До свидания")
