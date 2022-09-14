goal = int(input("Число: "))

power = 1

while goal >= 2 ** (power + 1):
    power += 1

print(power, 2**power)
