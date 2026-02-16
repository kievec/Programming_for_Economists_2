# we will open the file, and read from it

try:
    fd = open("text.txt")
    print("File opened")
    # we can use the read method
    print(fd.read())
    print("File read")
    fd.close() # shows that we are done
except FileNotFoundError:
    print("Sorry, file not found")

# another simpler way (more pythonic)
with open("text.txt", "r") as fd:
    print(fd.read())

# "r" means to read

# smarter way to read, line by line
with open("text.txt", "r") as fd:
    for line in fd:
        # print(line) adds 2 enters!
        # print(line, end="")
        print(line.strip()) # strip method removes new line at the end