# Operators (Arithmetic)
print(3+5) #addition
print(5-2) #subtraction
print(3*5) #multiplication * is multiply
print(4/2) #division, always returns float!
# #(since div has no gurantee of integer answers, thus all divisions will have a decimal point)

print(4//2) #integer division! will have no decimal point
print(9%2) #shows the remainder
print(9**2) #power

print(4==4.0) #comparison operator is double ==, a single = is assigning value
print(3!=4.0) #is it not equal?

#Boolean operators (Logic)
# Or only requires to meet ONE of the parameters
# And requires to sequentially validate ALL the parameters

# Everything in Python is considered TRUE, unless:
# 0, 0.0, False, None, [], (), {}
# anything that returns those values will be FALSE

print(True or False)  #True
print(True and False) #False
print((7 < 10) or (100 < 10)) #TRUE since one of them satisfies the condition
print(7 or 6)
print(7 and 6)
print(0 or None or False or 22 or 0.0) # result will be 22, the first (non-false like value)
# it will be the right answer
# if the chain of or's and all are FALSE, result is the LAST False
print(11 and 22 and None and 17) #the result is None, stop at the first false like value
# if the chain of and's is all TRUE, the result is the LAST one

print((6 or 9) and ("bob" or "joe")) #bob is the result

# the result is when did you know, when did you stop?

# not is always TRUE/FALSE
print(not 7) # 7 is True and opposite of that is False
print(not "") # True, opposite of opposite is True

#Operators
print(3 <100) #Less than
print(3 <= 3) # less or equal
print((26*3)>(10*4))
print("3 letter combinations", 26**3, "vs 4 digit combinations", 10**4)

A = 3
A+=1 #increment existing A by 1

#Paranthesis makes things cleaners