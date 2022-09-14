fstring = input("Строка: ")

r = fstring.rfind("f")
l = fstring.find("f")

print(r if r == l else f"{l} {r}")
