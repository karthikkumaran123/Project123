import re

def display_payment_option():
    print("Payment Options: ")
    print("1. Debit Card")
    print("2. Credit Card")
    print("3. Cash On Delivery")

display_payment_option()

ChoosePaymentOption = input("Select Your Payment Method: ")

cardnum_pattern = r'^\d{8}$'
expiry_pattern = r'^(0[1-9]|1[0-2])/(2[2-9]|3[0-9])$'
Cvv_pattern = r'^\d{3}$'

if ChoosePaymentOption == "1":
    CardNum = input("Enter Debit Card Number: ")
    ExpiryDate = input("Expiry Date (MM/YY): ")
    CvvNum = input("CVV : ")
    if re.match(cardnum_pattern, CardNum) and re.match(expiry_pattern, ExpiryDate) and re.match(Cvv_pattern, CvvNum):
        print("Payment Successful")
    else:
        print("Invalid Credentials. Please provide valid details.")
        CardNum = input("Enter Debit Card Number: ")
        ExpiryDate = input("Expiry Date (MM/YY): ")
        CvvNum = input("CVV : ")
elif ChoosePaymentOption == "2":
    CardNum1 = input("Enter Credit Card Number: ")
    ExpiryDate1 = input("Expiry Date (MM/YY): ")
    CvvNum1 = input("CVV : ")
    if re.match(cardnum_pattern, CardNum1) and re.match(expiry_pattern, ExpiryDate1) and re.match(Cvv_pattern, CvvNum1):
        print("Payment Successful")
    else:
        print("Invalid Credentials. Please provide valid details.")
        CardNum1 = input("Enter Credit Card Number: ")
        ExpiryDate1 = input("Expiry Date (MM/YY): ")
        CvvNum1 = input("CVV : ")
elif ChoosePaymentOption == "3":
    print("Due to handling costs, a nominal fee of ₹10 will be charged.")

deliveryorder1 = "CONFIRM ORDER"
deliveryorder2 = "CANCEL"

print(f"{deliveryorder1} / {deliveryorder2}")
print("Confirm Cash on delivery order: ")
deliveryorder = input()
if deliveryorder == deliveryorder1:
    print("THANKS FOR CONFIRMING YOUR ORDER! KEEP SHOPPING WITH US..!! ")
elif deliveryorder == deliveryorder2:
   print("ORDER CANCELED. THANK YOU..!!")

