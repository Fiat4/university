h1, m1, s1 = map(int, [input("") for i in range(3)])

h2, m2, s2 = map(int, [input("") for i in range(3)])

h_diff = h2 - h1
m_diff = m2 - m1
s_diff = s2 - s1

print(h_diff * 3600 + m_diff * 60 + s_diff)
