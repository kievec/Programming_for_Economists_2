name = input("Enter your name: ")
print("Hello", name)

age = input("Enter your age: ") #input from user is ALWAYS treated as a string
try:
    age = int(age)
    print("you were born in", 2025-age)

except ValueError:
    print("I am sorry", name, "but that is not a real number")
except ZeroDivisionError:
    print("You can't divide by zero")
else: # else is only when no exception happens
    print("Thank you for playing fair")
finally:
    print("End of Game") # this one happens no matter what

# Catching Exceptions
# 1. Syntax Error - its just flat out wrong