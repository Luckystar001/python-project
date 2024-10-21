# string method 
# task- validate user input exercise
# username must not be more than 12 characters
# username must not contain spaces
# username must not contain digits


username = input("Enter your Username  ")
if len(username) > 12:
    print("Your username cant't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Spaces are not allowed")
elif not username.isalpha():
    print("Digits are not allowed")
