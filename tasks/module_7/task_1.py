words = input("Строка: ").split()

collection: dict[str, int] = {}

for word in words:
    if word in collection:
        print(collection[word], end=" ")
        collection[word] += 1
    else:
        print(0, end=" ")
        collection.update({word: 1})
