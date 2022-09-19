count = int(input("Кол-во: "))

words: dict[str, int] = {}

for _ in range(count):
    for word in input("").split():
        words[word] = words.get(word, 0) + 1

maximum = 0
mwords = []

for key, value in words.items():
    if value > maximum:
        maximum = value
        mwords = [key]
    elif value == maximum:
        mwords.append(key)

print(sorted(mwords)[0])
