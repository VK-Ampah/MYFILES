# Comment like a pro: store contstant ion data file to use and update values
# Import libraries
import datetime
CurrDate = datetime.datetime.now()
# Open the defaults file and read the values into variables
f = open('Def.dat', 'r')
MovieNum = int(f.readline())
HSTRate = float(f.readline())
NewRelDays = int(f.readline())
ObsWeeks = int(f.readline())
f.close()
# Define required functions
# Main program
while True:
    MovieName = input("Enter tne movie name (Type End to quit): ").title()
    if MovieName == "End":
        break
    MovieType = input("Enter the movie type (D, C, M, H): ").upper()
    MovieRating = input("Enter the movie rating (G, P, R): ").upper()
    RentalCost = float(input("Enter the rental cost (1.99 - 8.99): "))
    # Add any calculations here if required.
    # Display the claim receipt on the screen.
    print(MovieNum)
    print(MovieName)
    print(MovieType)
    print(MovieRating)
    print(RentalCost)
    # Write the claim data to a text file.
    print()
    print("Saving movie data for " + MovieName + ".  Please wait ...")
    f = open("Movies.dat", "a")
    f.write(f"{str(MovieNum)}, ")
    f.write(f"{MovieName}, ")
    f.write(f"{MovieType}, ")
    f.write(f"{MovieRating}, ")
    f.write(f"{str(RentalCost)}\n")
    f.close()
    # Put a progress bar or something similar to let the user know something is happening.
    print()
    print("Movie information has been successfully saved ...")
    MovieNum += 1
    # Write the current values back t the default file. Note the use of “w” to overwrite and the use of
    # the \n so that each value is placed on a separate line.
    f = open('Def.dat', 'w')
    f.write(f"{str(MovieNum)}\n")
    f.write(f"{str(HSTRate)}\n")
    f.write(f"{str(NewRelDays)}\n")
    f.write(f"{str(ObsWeeks)}\n")
    f.close()