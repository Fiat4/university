numbers = [int(x) for x in input("Последовательность: ").split()]

count = len(numbers)

for i in range(0, count - 1, 2):
    print(numbers[i + 1], numbers[i], end=" ")

if count % 2 != 0:
    print(numbers[count - 1])
