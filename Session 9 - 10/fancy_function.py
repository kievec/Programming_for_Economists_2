def add_numbers(a, b, c=0):
    return a + b + c

print(add_numbers(5,8, 9))
print(add_numbers(b=7, c=11, a=-100)) # call by name

# a function that calls itself is called recursive!
# factorial of n = n X factorial of n - 1
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(10))

# functions can call other functions
# the name is bond, james bond

def greeting(name):
    return f"The name is: {name}!"

def bond_name(first, last):
    return f"{last}, {first} {last}"

print(greeting("Sanchez, Maria Sanchez"))
print(greeting(bond_name("Jerry", "Bond")))