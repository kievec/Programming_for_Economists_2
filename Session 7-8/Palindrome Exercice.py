from string import punctuation

s = "Red Roses run no risk, sir on nurses order"
# prove that this sentence is a palindrome!"
# 1. sanitize (remove space and remove other punctuation)
# 2. make it all same case (lower or uppercase) . use .lower() method
# 3. compare that the slice of reverse is the same as the original

punctuation = " !?,."
for p in punctuation:
    s = s.replace(p, "")
print(s)
s = s.upper()
print(s)
if s == s[::-1]:
    print("Yes")
else:
    print("No")