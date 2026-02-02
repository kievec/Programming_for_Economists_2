# you can assign a string to a variable
s1 = "hello"
s2 = "bye"

# you can add 2 strings
print(s1 +s2)

# you can multiply a string via an integer!
print(s1*3)

s1 = "I am very angry"
s2 = "!"*20
print(s1 + s2)

# you can iterate over a string via for!!
for c in s1:
    print(c) # it prints letter by letter

s2 = ""
for c in s1:
    s2 = s2 + c*5
print(s2)

for c in s1:
    if c == "":
        print("?", end )