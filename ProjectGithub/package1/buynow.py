import re
def choose_product_option():
    print("Order Summary")
product_options = {
        "1" : "option1 : AllenSolly-ASSFQMOB902023",
        "2" : "option2 : PeterEngland-PCSFSSLPK66318",
        "3" : "option3 : Adidas-FJ2212",
        "4" : "option4 : Gucci-AJ0032"
    }
print(product_options)
choice =input("Enter the number of your choice: ")
if choice == "1":
    print("Confirm to BuyNow..!"
          "Free Delivery"
          "10 Days Return Policy"
          "Cash on delivery Available")
elif choice == "2":
    print("Confirm to BuyNow..!"
          "Discount offer:35% off"
          "Delivery in 2 days"
          "Coupon Code Accepted")
elif choice == "3":
    print("Confirm to BuyNow..!"
          "Free Delivery"
          "10 days return policy")
elif choice == "4":
    print("Confirm to BuyNow..!"
          "Discount offer: 40%off"
          "Delivery in 3 days")
else:
    print("Invalid choice.Please Select a valid option: (1/4).")
    print(product_options)

choose_product_option()

# Order Summary
# first step delivery address

print("ADD DELIVERY ADDRESS")
username_pattern =  r'^[a-zA-Z0-9]+$'
username = input("Full Name (Required)* - ")
while True:
 if re.match(username_pattern, username):
    break
 else:
    print("Username is Incorrect.Please Enter a Valid Username.")
    username = input("Full Name (Required)* - ")

phonenum_pattern = r"\d{3}-\d{3}-\d{4}"
phonenumber = input("Phone Number (Required)* - ")
while True:
 if re.match(phonenum_pattern,phonenumber):
    break
 else:
    print("Phonenumber is Incorrect.Please Enter a Valid Phonenumber.")
    phonenumber = input("Phone Number (Required)* - ")

pincode_pattern = r"^\d{3}-\d{3}$"
pincode = input("Pincode (Required)* - ")
while True:
 if re.match(pincode_pattern,pincode):
    break
 else:
     print("Pincode is Incorrect.Please Enter a Valid Pincode.")
     pincode = input("Pincode (Required)* - ")
State = input("State (Required)* - ")
city = input("City (Required)* - ")
House = input("House No,Building Name (Required)* - ")
Root = input("Road name, Area, Colony(Required)* - ")

# type of address
print("TYPE OF ADDRESS")
choose = input("Home/Work : ")
print("Address Saved")



