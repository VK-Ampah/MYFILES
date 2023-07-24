# Comment like a pro.
# Import required libraries
import datetime
import FormatValues as FV
CurrDate = datetime.datetime.now()
# Before the loop: Print headings, Initialize summary data, Open the file.
print()
print(" "*21, "WIDGITS INCORPORATED")
print()
print(f"       ACCOUNTS RECEIVABLE SUMMARY REPORT AS OF {FV.FDateS(CurrDate)}")
print()
print(" ACCOUNT      CUSTOMER           BALANCE    CREDIT      MINIMUM")
print(" NUMBER         NAME               DUE     REMAINING    PAYMENT")
print("", "="*62)
TotCustCtr = 0
BalDueAcc = 0
MinPayAcc = 0
f = open("Customers.dat", "r")
for CustDataLine in f:
    # Inside the loop, Read the record, do any calculations, print the detail line.
    CustLine = CustDataLine.split(",")
    # All fields in the list are strings.
    # Numbers and dates must be parsed.
    # Only grab the values from the list that are required.
    CustNum = CustLine[0].strip()
    CustName = CustLine[1].strip()
    BalDue = float(CustLine[5].strip())
    CredLim = float(CustLine[6].strip())
    # Perform any required calculations here.
    CredRem = CredLim - BalDue
    if BalDue <= CredLim:
        MinPay = BalDue * .10
    else:
        MinPay = (BalDue * .10) + (BalDue - CredLim)
    # Print the detail line.
    print(f" {CustNum:>5s}   {CustName:<20s}  {FV.FDollar2(BalDue):>9s}   {FV.FDollar2(CredRem):>9s}  {FV.FDollar2(MinPay):>9s}")
    # Increment any counters or accumulators.
    TotCustCtr += 1
    BalDueAcc += BalDue
    MinPayAcc += MinPay
# After the loop, close the file, and print the summary data.
f.close()
print("", "="*62)
print(f" Customers listed: {TotCustCtr:>3d}        {FV.FDollar2(BalDueAcc):>10s}             {FV.FDollar2(MinPayAcc):>10s}")
print()
print(" "*24, "END OF LISTING")