num = 1
while num <= 100:
    print(num)
    num += 1

import random
money = 10000
counter = 1
while money > 0:
    print(money)
    expense = random.randint(1, 100)
    print("Iteration", counter, "expense=", expense)
    counter = counter + 1
    money = money - expense