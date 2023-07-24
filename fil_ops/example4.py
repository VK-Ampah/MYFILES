# Comment like a pro: use f string
# Import libraries
import datetime
CurrDate = datetime.datetime.now()
import FormatValues as FV
# Define constants
INV_NUM = 1358
# Define required functions

# Main program
while True:
    CustName = input("Enter the customer name: ").title()
    CustPhone = input("Enter tne phone number (9999999999): ")
    BikeType = input("Enter the type of bicycle (T / M): ").upper()
    NumBikes = int(input("Enter the number of bicycles rented (1 - 3): "))
    CCNum = input("Enter the credit card number (9999999999999999): ")
    ExpDate = input("Enter the expiry date (MM/YY): ")
    print()
    print("Please wait - writing data to rentals table.")
    f = open("Rentals.dat", "a")
    f.write(f"{str(INV_NUM)}, ")
    f.write(f"{CustName}, ")
    f.write(f"{CustPhone}, ")
    f.write(f"{BikeType}, ")
    f.write(f"{str(NumBikes)}, ")
    f.write(f"{CCNum}, ")
    f.write(f"{ExpDate}\n")
    f.close()
    print()
    print("Save successful.")
    INV_NUM += 1
    print()
    Continue = input("Do you want to enter another rental (Y / N): ").upper()
    if Continue == "N":
        break
    print()  # Back to the top to start all over again.