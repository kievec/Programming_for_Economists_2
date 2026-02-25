a = [1, 2, 3]
a.append("John")
a.append("Doe")
print(a)

# extend is same as +
a1 = [1, 2, 3]
a2 = [4, 5, 6]
a2.extend(a1)
print(a2)
a2.sort()
print(a2)