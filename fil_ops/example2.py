# Comment like a pro
# Import libraries
import datetime
CurrDate = datetime.datetime.now()
import FormatValues as FV
# Define constants
CLAIM_NUM = 34
HST_RATE = .15
# Define required functions
# Main program
while True:
    EmpNum = input("Enter the employee number (99999 - Type END to quit): ")
    if EmpNum.upper() == "END":
        break
    EmpFirst = input("Enter the employee first name: ").title()
    EmpLast = input("Enter the employee last name: ").title()
    Location = input("Enter the trip location: ").title()
    StartDate = input("Enter the start date (YYYY-MM-DD): ")
    StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
    EndDate = input("Enter the end date (YYYY-MM-DD): ")
    EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
    OwnRent = input("Did you use your own car or rent (O / R): ").upper()
    TotalKilo = 0
    if OwnRent == "O":
        TotalKilo = int(input("Enter the total kilometers: "))
    NumDays = (EndDate - StartDate).days
    if NumDays >= 3:
        PerDiem = NumDays * 85.00
    else:
        PerDiem = NumDays * 100.00
    if OwnRent == "O":
        Mileage = TotalKilo * .10
    else:
        Mileage = NumDays * 56.00
    ClaimAmt = PerDiem + Mileage
    HST = ClaimAmt * HST_RATE
    ClaimTotal = ClaimAmt + HST
    # Display the claim receipt on the screen.
    print(NumDays)
    print(PerDiem)
    print(Mileage)
    print(ClaimAmt)
    print(HST)
    print(ClaimTotal)
    # Write the claim data to a text file.
    f = open("Claims.dat", "a")  # Mode at the end indicates what you want to do.
    f.write("{}, ".format(str(CLAIM_NUM)))
    f.write("{}, ".format(str(CurrDate)))  # This is the current system date
    f.write("{}, ".format(EmpNum))
    EmpName = EmpFirst + " " + EmpLast
    f.write("{}, ".format(EmpName))  # Could also have written both EmpFirst and EmpLast.
    f.write("{}, ".format(Location))
    f.write("{}, ".format(StartDate))
    f.write("{}, ".format(EndDate))
    f.write("{}, ".format(str(NumDays)))
    f.write("{}\n".format(str(ClaimTotal)))  # All numbers or dates need to be converted to Strings.
    f.close()
    # Put a progress bar or something similar to let the user know something is happening.
    print()
    print("Claim information has been successfully saved ...")
    CLAIM_NUM += 1
    # Go look up a video on the difference between a text file (often called a Flat File) and a database.