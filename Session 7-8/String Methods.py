s = "hello world!"
print(dir(s))

print(help(s.capitalize))
print("heLLO WORLd!".capitalize()) # it only capitalises the first leter

print(help(s.center))
print("BOB".center(22,"*"))

# find finds the position where a substring can be found!
s = "I see a cat on the street. The street is nice. The cat is black"
print("The position of cat is", s.find("cat"))
print("The next position of cat is", s.find("cat", 9))
print("find returns -1 if we can not find it:", s.find("dog"))

emails = "bob@gmail.com and then we have alice@yahoo.com and we can also have james@facebook.co.uk and that's it"
print(emails.count("@"))
pos = 0
while True:
    pos = emails.find("@", pos)
    if pos == -1:
        break
    print("Found one email at position", pos)
    pos += 1

# replace will replace part of a string with another one
print(s)
print(s.replace("cat", "parrot"))
print(s.replace("","|"))

# split will break the string into components based on the key!
print(s.split())
