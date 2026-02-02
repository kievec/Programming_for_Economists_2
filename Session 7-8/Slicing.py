s = "hello world!"
print(s[5]) # indexing, one letter

# slide 1, from start to end
print(s[2:7]) # end if excluded! so only 5 characters, not 6!!
print(s[3:5])
# you can omit the start or the end or both
print(s[:7]) # from beginning to position 7 excluded!
print(s[3:]) # from pos 3 to the end
print(s[:]) # the entire string

# adding steps
print(s[::2])
print(s[4::3])
print(s[::-1]) # reverse string