import secrets
import string


N = 5
#Generates a random sequence of letters and digits of any length,
#In our case the length is equal to N which is set to five
res = ''.join(secrets.choice(string.ascii_lowercase + string.digits)for i in range(N))

def User_Validation(firstName, lastName, email):
    randomPassword = firstName[:2] + lastName[-2:] + str(res)
    print(f"\nThis is your password:{randomPassword}")
    answer = input("\nAre you satisfied with it ? Yes or No\n>")

    while answer.lower() != "yes" and  answer.lower() != "no":
        answer = input("Please answer Yes or No !")

    if answer.lower() == "no":
        password = input("Create your password :")
        while len(password) < 8:
            print("Your password must be 8 characters or more")
            password = input("Create another password :")
        userGeneratedCredentials = {
               'First Name' : firstName,
               'Last Name' : lastName,
               'Email Address' : email,
               'Password' : password
        }
        print("\nPassword created successfully.")
        print("Your data has been validated.\n")
        for field, credential in list(userGeneratedCredentials.items()):
            print(f"Your {field} is {credential}")

        secondUser = input("\nWould you like to try another user ? Yes or No\n>")

        while secondUser.lower() != "yes" and secondUser.lower() != "no":
            secondUser = input("Please answer Yes or No")

        # This will call the User_Validation function again if secondUser == yes
        if secondUser.lower() == "yes":
            User_Validation(input("Please enter your first name ?\n"), input("\nEnter your last name?\n"), input("\nEnter your email address ?\n"))
        else:
            print("Thank you for your time")

    else:
        randomGeneratedCredentials = {
               'First Name' : firstName,
               'Last Name' : lastName,
               'Email Address' : email,
               'Password' : randomPassword
        }
        print("\nPassword created successfully.")
        print("Your data has been validated.\n")
        for field, credential in list(randomGeneratedCredentials.items()):
            print(f"Your {field} is {credential}")

        anotherUser =  input("\nWould you like to try another user ? Yes or No\n>")

        while anotherUser.lower() != "yes" and anotherUser.lower() != "no":
            anotherUser = input("Please answer Yes or No")
               
        # As in line 37, the function is called again if anotherUser == yes
        if anotherUser.lower() == "yes":
            User_Validation(input("Please enter your first name ?\n"), input("\nEnter your last name?\n"), input("\nEnter your email address ?\n"))
        else:
            print("Thank you for your time")


User_Validation(input("Please enter your first name ?\n"), input("\nEnter your last name ?\n"), input("\nEnter your email address ?\n"))
