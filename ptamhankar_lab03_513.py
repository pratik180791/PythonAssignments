import datetime
import time
now=datetime.datetime.now()
print("Hello and welcome to Lab03\n");
pin_system="PT1807"
flag=False;
count=2
pin_entered=input("\nPlease enter your PIN to proceed: ")
ifcontinue="Y"
while (pin_entered != pin_system) and count != 0:

                pin_entered=input("\nInvalid input,Please enter a valid pin "+str(count)+" attempts left: ")
                count = count - 1

if count==0:
            print("\nMaximum attempts reached for PIN input, please try again later!")


else:
    print("PIN Validated")

    while(ifcontinue=="Y" or ifcontinue=="y"):

        initial_balance=int(input("\nPlease enter your initial deposit amount:"))
        interest_rate=(int(input("\nPlease enter a valid annual interest rate:")))/100

        print(interest_rate)
        month=0
        new_balance=initial_balance

        while month!=12:
                new_balance=new_balance+((interest_rate/12)*new_balance)
                month = month + 1
                print("Month "+str(month)+" , new balance:"+str(new_balance))

        print("\nHi, DO you wish to continue?, Y or N")
        ifcontinue=input("\nDo you wish to continue ?(Y/N)")

if ifcontinue!="Y":
 print("\nThank you for banking with us")

print(now.strftime("%Y-%m-%d %H:%M"))
print("\n")
print("Programmed by Pratik Tamhankar")