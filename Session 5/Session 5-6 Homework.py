gross = input("Enter gross salary: ")
children = input("Enter number of children: ")

try:
    gross = float(gross)
    children = int(children)
except ValueError:
    print("Invalid input")
    exit()

if gross < 1000:
    tax_rate = 0.10
elif gross < 2000:
    tax_rate = 0.12
elif gross < 4000:
    tax_rate = 0.14
else:
    tax_rate = 0.18

if gross < 2000:
    tax_rate = tax_rate - (0.01 * children)
elif gross > 2000:
    tax_rate = tax_rate - (0.005 * children)

if tax_rate < 0:
    tax_rate = 0

net = gross * (1 - tax_rate)
print(net)
