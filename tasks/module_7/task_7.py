count = int(input("Кол-во: "))

words: dict[str, int] = {}

for _ in range(count):
    for word in input("").split():
        words[word] = words.get(word, 0) + 1

for key in sorted(words, key=words.get, reverse=True):  # type: ignore
    print(key, words[key])
