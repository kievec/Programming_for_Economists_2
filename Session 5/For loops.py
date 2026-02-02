n = 0 # initial state
while n < 10:
    print(n)
    n = n + 1

#range does the initial state and increment after each iteration
for i in range(10):
    print(i)

for i in range(0, 10, 1): # explicit, 0 is default start, + 1 is default increment
    print(i)

for i in range(0, 100, 10): print(i) #start, end & increment

for i in range(10):
    print(i*10)

# print multiplication table until 10
for i in range(1,11):
    for j in range(i,11):
        print(f"{i} x {j} = {i*j}") # the f string allows you to put values inside
    print()
