words = input("Строка: ").split()

collection: dict[str, int] = {}

for word in words:
    cw = collection.get(word, 0)
    print(cw, end=" ")
    collection[word] = cw + 1
