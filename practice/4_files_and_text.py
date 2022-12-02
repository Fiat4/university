def read_file(filename: str) -> set[str]:
    words = set()
    translation = str.maketrans(dict.fromkeys(map(ord, ".,!:?"), None))
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            [words.add(word.lower().translate(translation)) for word in line.split()]
    return words


def save_file(filename: str, words: list[str]) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Всего уникальных слов: {len(words)}\n")
        f.write("=====================\n")
        f.write("\n".join(words))


words = read_file("data/data.txt")
save_file("data/count.txt", sorted(words))
