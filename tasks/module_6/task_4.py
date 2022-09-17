numbers: list[int] = [int(x) for x in input("Последовательность: ").split()]

minimum_index = numbers.index(min(numbers))
maximum_index = numbers.index(max(numbers))

numbers[minimum_index], numbers[maximum_index] = (
    numbers[maximum_index],
    numbers[minimum_index],
)

print(" ".join(map(str, numbers)))
