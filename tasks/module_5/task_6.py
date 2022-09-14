number = int(input("Число: "))

index = 1
fib = [0, 1]

while number >= (f := fib[0] + fib[1]):
    fib[0], fib[1] = fib[1], f
    index += 1

print(index if number == fib[0] + fib[1] else -1)
