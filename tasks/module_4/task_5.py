print(
    "Да"
    if any(
        map(lambda x: x < 0, map(int, [input(f"Число {x}: ") for x in range(1, 2 + 1)]))
    )
    else "Нет"
)
