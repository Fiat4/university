numbers = [int(x) for x in input("Последовательность: ").split()]

for number in numbers:
    if number % 2 != 0:
        print(number, end=" ")
