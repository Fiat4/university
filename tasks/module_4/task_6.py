number = input("Число: ")

print("Да" if "".join(sorted(list(number))) == number else "Нет")