numbers = [int(x) for x in input("Последовательность: ").split()]

for index, value in enumerate(numbers[1:]):
    if value > numbers[index]:
        print(value, end=" ")
