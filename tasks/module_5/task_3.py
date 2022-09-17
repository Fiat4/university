start = int(input("Стартовая скорость: "))
distance = float(input("Дистанция: "))

days = 0

while distance > 0:
    distance -= start * (1 + 0.1) ** days
    days += 1

print(days)
