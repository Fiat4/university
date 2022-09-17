string = input("Строка: ")

first = string.find("h")
last = string.rfind("h")
new_string = list(string.replace("h", "H"))
new_string[first], new_string[last] = "h", "h"

print("".join(new_string))
