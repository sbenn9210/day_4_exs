
palindrome_input = input("Please enter a palindrome: ")



if palindrome_input == palindrome_input[::-1]:
    print("Correct, that is a palindrome")
else:
    print("Wrong, that is not a palindrome ")
