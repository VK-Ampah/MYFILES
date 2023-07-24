#  Comments
# Import Libraries
import matplotlib
import datetime

# Define constants
BONUS_RATE = .01


# Define functions
def CalcBonus(TotalSales) :
    # Calculate the bonus and the status and return both values as a Tuple.
    Bonus = TotalSales * BONUS_RATE
    if TotalSales < 5000.00 :
        Bonus -= (5000.00 - TotalSales) * .17
        Status = "Under"
    elif TotalSales > 100000.00 :
        Bonus += 500.00
        Status = "Extraordinary"
    else :
        Status = "Normal"
    return Bonus, Status


# Main program
'''
TotalSales = 8000.00
BonStat = CalcBonus(TotalSales)
print(BonStat)
print(BonStat[0])
print(BonStat[1])
# To access a list use LstName(index).
# To access a tuple use TupleName[index].
'''
while True :
    # set up required suer inputs
    while True :
        ListingNum = input("Enter the listing number (999999999): ")
        if ListingNum == "" :
            print("Error - Listing number cannot be blank - Please reenter.")
        elif len(ListingNum) != 9 :
            print("Error - Listing number must be 9 characters - Please reenter.")
        elif not ListingNum.isdigit() :
            print("Error - Listing number must be 9 digits - Please reenter.")
        else :
            break
    StAdd = input("Enter the street address: ")
    while True :
        try :
            NumBed = int(input("Enter the number of bedrooms: "))
        except :
            print("Error - Number of bedrooms must be a valid number - Please reenter.")
        else :
            break
    NumBath = int(input("Enter the number of bathrooms: "))
    TotSqFt = int(input("Enter the total square footage: "))
    PriceLst = [ ]
    DateLst = [ ]
    while True :
        while True :
            try :
                ListingPrice = float(input("Enter the listing price (-1 to end): "))
            except :
                print("Error - Listing price must be a valid number - Please reenter.")
            else :
                break
        if ListingPrice == -1 :
            break
        while True :
            try :
                ListingDate = input("Enter the listing date (YYYY-MM-DD): ")
                ListingDate = datetime.datetime.strptime(ListingDate, "%Y-%m-%d")
            except :
                print("Error - Listing price not a valie date - Please reenter.")
            else :
                break

        PriceLst.append(ListingPrice)
        DateLst.append(ListingDate)

    StatusLst = [ "Open", "Offer Pending", "Sold" ]
    while True :
        Status = input("Ether the home status (Open, Offer Pending, Sold): ").title()

        if Status == "" :
            print("Error - Status cannot be blank - Please reenter.")
        elif Status not in StatusLst :
            print("Error - Status must be Open, Offer Pending, or Sold - Please reenter.")
        else :
            break

    # Calculations if there are any.

    # Display results
    print(f"Listing number:          {ListingNum}")
    print(f"Street address:          {StAdd}")
    print(f"Number of bedrooms:      {NumBed}")
    print(f"Number of bathrooms:     {NumBath}")
    print(f"Total square footage:    {TotSqFt}")
    print()
    # print the listing prices and the dates from the lists.

