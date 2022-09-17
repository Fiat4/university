numbers = [int(x) for x in input("Последовательность: ").split()]

seen = set()

for number in numbers:
    if number in seen:
        print("ДА")
    else:
        print("НЕТ")
        seen.add(number)
