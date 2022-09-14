a, b, c = map(int, [input(f"Число {i+1}: ") for i in range(3)])

if a == b == c: print(3)
elif any([a == b, c==b, a==c]): print(2)
else: print(0)