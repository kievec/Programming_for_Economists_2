s1 = "hello world"
s2 = 'hello world'

print(s1)
print(s2)

s1 = "hello world @&#&@&*@#"
print(s1)
# I can print individual components
print(s1[1]) # start counting from 0!! the bracket shows the position of the character
print(s1[4])
print(s1[-1])  #last character !!
print(s1[-4]) # prints &

print(len(s1))  # the amount of characters in the string
print(s1[len(s1)-1])  # the last character, instead of -1

# index needs to be integer!
print(8/4)
print(s1[8*2])
