cities: dict[str, str] = {}

for _ in range(int(input("Кол-во стран: "))):
    cities_raw = input().split()
    for city in cities_raw[1:]:
        cities[city] = cities_raw[0]

output: list[str] = []

for _ in range(int(input("Кол-во поисков: "))):
    output.append(cities.get(input(), "Не найден"))

print("\n".join(output))
