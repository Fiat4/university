y, x, u, c = map(int, [input(f"Число {i+1}: ") for i in range(4)])

print("Да" if (x+y) % 2 == (c+u) % 2  else "Нет")
