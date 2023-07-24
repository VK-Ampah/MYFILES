# Comment like a pro: Program with defaults file and data file for the Conference center.
# Import required libraries
import datetime
# Open the defaults file and read the values into variables
f = open('defaults.dat', 'r')
NEXT_CONF_NUM = int(f.readline())
HST_RATE = float(f.readline())
COST_SMALL = float(f.readline())
COST_MED = float(f.readline())
COST_LARGE = float(f.readline())
COST_BREAKFAST = float(f.readline())
COST_LUNCH = float(f.readline())
COST_SUPPER = float(f.readline())
COST_COFFEE = float(f.readline())
f.close()
# Define required functions
#Main Program
while True:
    ClientName = input("Enter the client name (END to quit): ").title()
    if ClientName == "End":
        break
    ConfTitle = input("Enter the conference title: ").title()
    StartDate = input("Enter the start date (YYYY-MM-DD): ")
    StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
    NumAtt = int(input("Enter the number of attendees: "))
    NumDays = int(input("Enter the number of days: "))
    NumBreakfast = int(input("Enter the number of breakfasts: "))
    NumLunch = int(input("Enter the number of lunches: "))
    NumSupper = int(input("Enter the number of suppers: "))
    NumCoffee = int(input("Enter the number of coffee breaks: "))
    if NumAtt <= 30:
        CostRoom = NumDays * COST_SMALL
    elif NumAtt <= 100:
        CostRoom = NumDays * COST_MED
    else:
        CostRoom = NumDays * COST_LARGE
    CostBreak = NumAtt * COST_BREAKFAST * NumBreakfast
    CostLunch = NumAtt * COST_LUNCH * NumLunch
    CostSupper = NumAtt * COST_SUPPER * NumSupper
    CostCoffee = NumAtt * COST_COFFEE * NumCoffee
    ConfCost = CostRoom + CostBreak + CostLunch + CostSupper + CostCoffee
    HST = ConfCost * HST_RATE
    ConfTotal = ConfCost + HST
    CostPerAtt = ConfTotal / NumAtt
    print(CostRoom)
    print(CostBreak)
    print(CostLunch)
    print(CostSupper)
    print(ConfCost)
    print(HST)
    print(ConfTotal)
    print(CostPerAtt)
    print()
    print("Saving conference data ...")
    # Add a progress bar or reasonable option here.
    # Write the values to a file for future reference.
    f = open("Stuff.dat", "a")
    f.write(f"{NEXT_CONF_NUM}, ")
    f.write(f"{ClientName}, ")
    f.write(f"{ConfTitle}, ")
    f.write(f"{NumAtt}, ")
    f.write(f"{ConfTotal}\n")
    f.close()
    print("Conference data successfully saved ...")
    # Update any default values based on the processing requirements
    NEXT_CONF_NUM += 1
    # Housekeeping
    # Write the current values back t the default file. Note the use of “w” to overwrite and the use of
    # the \n so that each value is placed on a separate line.
    f = open('defaults.dat', 'w')
    f.write(f"{NEXT_CONF_NUM}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{COST_SMALL}\n")
    f.write(f"{COST_MED}\n")
    f.write(f"{COST_LARGE}\n")
    f.write(f"{COST_BREAKFAST}\n")
    f.write(f"{COST_LUNCH}\n")
    f.write(f"{COST_SUPPER}\n")
    f.write(f"{COST_COFFEE}\n")
    f.close()