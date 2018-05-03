user_input = int(input("Enter a number: "))

a = 2

while user_input > a:
    if user_input % a == 0 and a != user_input:
        print("You did not enter a prime number")
        break
    a += 1
else:
    print("You entered a prime number")
