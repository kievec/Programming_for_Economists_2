# There are 3 ways to do an "if"
# 1. Simplest

name = input("Enter your name: ")
choice = input("Do you want a greeting? (y/n)")
if choice == "y":
    print("Hello " + name + "!")
    print("Good bye", name + "!")
print("Buenos dias", name + "!") # the if has no power here

