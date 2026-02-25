import random
a = random.randint(1, 10)
b = random.randint(1, 10)

print("a=", a)
print("b=", b)

if a > b:
    print("a > b")
elif a == b:
    print("a == b")
else:
    print("a < b")