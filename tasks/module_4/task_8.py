month = int(input("Месяц: "))

if month == 2: print(28)
else: 
    if month > 7: month -= 7
    print(31 if month %2 else 30)