# Comment like a pro: generate reports from a data file
# Import required libraries
# Before the loop: Print headings, Initialize summary data, Open the file.
print()
print(" " * 21, "WIDGITS INCORPORATED")
print()
print("             ACCOUNTS RECEIVABLE CUSTOMER LISTING")
print()
print("           ACCOUNT          CUSTOMER          PHONE")
print("           NUMBER             NAME            NUMBER")
print(" " * 10, "=" * 41)
TotCustCtr = 0
BalDueAcc = 0
f = open("Customers.dat", "r")
for CustDataLine in f :
    # Inside the loop, Read the record, do any calculations, print the detail line.
    CustLine = CustDataLine.split(",")
    # All fields in the list are strings.
    # Numbers and dates must be parsed.
    # Only grab the values from the list that are required.
    CustNum = CustLine [ 0 ].strip()
    CustName = CustLine [ 1 ].strip()
    PhoneNum = CustLine [ 4 ].strip()
    # Perform any required calculations here.
    # Print the detail line.
    print(f"           {CustNum:>5s}     {CustName:<20s}   {PhoneNum:<8s}")
    # Increment any counters or accumulators.
    TotCustCtr += 1

# After the loop, close the file, and print the summary data.
f.close()
print(" " * 10, "=" * 41)
print(f"           TOTAL CUSTOMER LISTED: {TotCustCtr:>2d}")