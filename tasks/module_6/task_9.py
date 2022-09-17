string = input("Строка: ")
length = len(string)

print(string[length // 2 + length % 2 :], string[: length // 2 + length % 2], sep="")
