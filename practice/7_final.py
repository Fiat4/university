def get_books(name: str) -> list[tuple[str, str, str, int, float]]:
    books = []
    name = name.lower()
    with open("data/books.csv", "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            isbn, title, author, quantity, price = line.strip().split("|")
            if name in title.lower():
                books.append((isbn, title, author, int(quantity), float(price)))
    return books


def get_totals(
    books: list[tuple[str, str, str, int, float]]
) -> list[tuple[str, float]]:
    response = []
    for book in books:
        price = book[3] * book[4]
        response.append((book[0], price if price >= 500 else price + 100))
    return response


print(get_totals(get_books("sample")))
