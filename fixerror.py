
import sys
while True:
    number=input("Enter the digits number")
    if number.isdigit() and len(number)==2:
        print("You are number",number)
    else:
        print("Try again")
    sys.exit("Thank! for playing game.")
    


    