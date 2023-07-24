# Comment like a pro : real estate tracking
# Import libraries
import datetime

CurrDate = datetime.datetime.now()
import FormatValues as FV

# Define constants

# Define required functions

# Main program
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
    print("Listing Price     Listing Date")
    print("------------------------------")
    for i in range(0, len(PriceLst)) :
        print(f"{FV.FDollar2(PriceLst [ i ]):>12s}     {FV.FDateS(DateLst [ i ]):>10s}")
    # Set up a progress bar to let the user know something is happening.
    print()
    print()
    Wait = input("Press the RETURN key to continue ...")
    print()
    import time
    from tqdm import tqdm

    print()
    print()
    print("Saving data - please wait")
    # Processing bar
    for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="{desc}  {bar}") :
        time.sleep(.1)

    # Write the record to the data file Homes.dat
    f = open("Homes.dat", "a")
    f.write(f"{str(ListingNum)}, ")
    f.write(f"{StAdd}, ")
    f.write(f"{str(NumBed)}, ")
    f.write(f"{str(NumBath)}, ")
    f.write(f"{str(TotSqFt)}, ")
    f.write(f"{PriceLst}, ")
    f.write(f"{DateLst}\n")
    f.close()
    print("Home data successfully saved ...")
    time.sleep(1)
    print()
    print()  # Back to the top to start all over again.
