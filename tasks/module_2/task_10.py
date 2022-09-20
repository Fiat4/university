print(
    sum(
        *[
            map(
                lambda x: x // 2 + x % 2,
                [int(input(f"Кол-во детей в классе {x}: ")) for x in range(1, 3 + 1)],
            )
        ]
    )
)
