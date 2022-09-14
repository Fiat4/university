palindrome = input("Строка: ")

print("Да" if palindrome == palindrome[::-1] else "Нет")