# Compute x**y using only additions

x = int(input("Insert integer x: "))
y = int(input("Insert integer y: "))

result = 1

for _ in range(y):
    temp = 0
    for _ in range(result):
        temp += x
    result = temp

print(result)