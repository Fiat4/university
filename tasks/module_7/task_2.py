count = int(input("Кол-во: "))

synonyms: dict[str, str] = dict([input().split() for _ in range(count)])

query = input("Ключ: ")

for key, value in synonyms.items():
    if query == key:
        print(value)
    elif query == value:
        print(key)
    else:
        continue
    break
