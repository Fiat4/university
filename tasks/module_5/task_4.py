last = float("inf")
count = 0

while (number := int(input("Число: "))) != 0:
    if number > last:
        count += 1
    last = number

print(count)
