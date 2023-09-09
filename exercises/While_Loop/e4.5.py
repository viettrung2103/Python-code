# Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied.
# The correct username is python and password rules.
USERNAME = "python"
PASSWORD = "rules"

input_user = input("username: ")
input_pw = input("password: ")
n = 0

while input_user != USERNAME or input_pw != PASSWORD :
    if n == 5: # at the 6th attempts
        print("you have 0 attempts left")
        print("Access denied")
        break
    else:
        print("Wrong credentials")
        print(f"n: {n}" )
        n = n+1
        input_user = input("username: ")
        input_pw = input("password: ")

else:
    print("Access granted!")
    print("Welcome!")
