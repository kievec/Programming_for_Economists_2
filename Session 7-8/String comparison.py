s1 = "banana"
s2 = "bob"

print(s1 > s2)
print("bob is greater than banana", s2 > s1)

# lowercase is always higher than uppercase
s1 = "banana"
s2 = "Banana" # the reason is due to ASCII table
print(s1 == s2)
print(s1 > s2)
print(s1 < s2)

# you always compare with ==

# we can use in operator with strings
# checks if smaller string is inside the bigger string
print("a" in "banana")
print("banana" in "banana")
print("bob" in "banana")

