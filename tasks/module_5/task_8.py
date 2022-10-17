last = float("inf")
count = 0
top = 0

while (number := int(input("Число: "))) != 0:
    if number == last:
        count += 1
    else:
        if top < count:
            top = count
        count = 1
    last = number

print(max(top, count))
