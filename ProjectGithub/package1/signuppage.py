# As a new user first create your account
print("CREATE ACCOUNT")
import re

class ForgetPassword:
    def email(self, email):
        self.email = email

        print("\n1. Enter the email address associated with your account."
              "\n2. A Password reset email is sent to your email address from flipkart@helpline.com",
              "\n3. Use this email to reset your password.")
        input("Enter your email address: ")
        print("\n1. Reset your password through this email."
              "\n2. Click the New Password."
              "\n3. Confirm the New Password.")
        newpassword = input("New Password: ")
        confirmpassword = input("Confirm New Password: ")
        if newpassword == confirmpassword:
            print("Password Reset Successfully.")
        else:
            print("Try Again.")
user_pattern = r'^[a-zA-Z0-9]+$'
password_pattern = r"^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[!@#$%&])(?=.[a-zA-Z!@#$%&]).{8,}$"
email_pattern = r'\b[A-Za-z0-9._%+-]+@gmail\.com$'
phonenum_pattern = r"\d{3}-\d{3}-\d{4}"

# Get the input values from the user
username = input("Name: ")
print("Create a new password")
password1 = input("Password: ")
useremail = input("Email: ")
phonenum = input("Phone Number: ")

if re.match(user_pattern, username) and re.match(email_pattern, useremail) and re.match(phonenum_pattern, phonenum):
    print("Account created successfully")
else:
    print("Incorrect credentials provided")
    print("Please try again")

# Login page
print("Login Page")
email = input("Email: ")
if useremail != email:
    print("Invalid Email Address. Please enter a valid Email Address.")
    name = input("Email: ")

password = input("Password: ")

if password1 == password:
    print("Login Successful.")

if password1 != password:
    print("Reset Password.")
    pw1 = ForgetPassword()
    pw1.email("self")
    print("Login Successful.")

# Return to homepage
print("WELCOME TO HOMEPAGE!!"
      "HAPPY SHOPPING..!")