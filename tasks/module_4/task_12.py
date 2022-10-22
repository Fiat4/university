def days_in_month(month: int):
    if month == 2:
        return 28
    else:
        if month > 7:
            month -= 7
        return 31 if month % 2 else 30


month = int(input("Месяц: "))
day = int(input("День: "))

if day + 1 > days_in_month(month):
    month += 1
    day = 1

print(f"{day}-{month}-2022" if month != 13 else "1-1-2023\n\nС Новым Годом!🎆")
