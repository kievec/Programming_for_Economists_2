def read_multiple_of_6():
    while True:
        try:
            num = int(input("Enter a multiple of 6: "))
            if num % 6 == 0:
                return num
            else:
                print("Not a multiple of 6")
        except ValueError:
            print("Please enter a valid integer")

result = read_multiple_of_6()
print(result)