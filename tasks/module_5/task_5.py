number = int(input("Число: "))

power = 1

while (a := power**2) < number:
    power += 1
    print(a, end=" ")
