user_input = int(input("Please choose a number: "))



def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    print(num)

factorial(user_input)
