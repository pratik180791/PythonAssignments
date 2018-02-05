import datetime
now=datetime.datetime.now()
print("Hello and welcome to the BMI Calculator\n") #Weclome message

choice=input("Please place your choice\n"
      "1:For entry in numeric metric unit format\n"
      "2:For entry in English metric unit format\n"); #Input prompt for choice

try:
    #Block for Numeric Metric Unit
    if(choice=='1'):
        weight_num=float(input("\nPlease enter your weight in Pounds:"))
        height_num=float(input("\nPlease enter your height in inches:"))

    #Block for English Metric Unit
    elif(choice=='2'):
                        weight_eng = float(input("\nPlease enter your weight in KG:"))
                        height_eng = float(input("\nPlease enter your height in Foot:"))
                        weight_num=weight_eng*2.204
                        height_num=height_eng*12
    else:
         print("Invalid input, please enter a valid choice:")

    #Calculation of BMI
    bmi = (weight_num * (703 / height_num ** 2));

    print("\nYour BMI value is:"+str(bmi)+" and you are,")

    if bmi < 18.5:
        print("UNDERWEIGHT")
    elif (bmi >= 18.5 or bmi <= 25):
        print("NORMAL weight");
    else:
        print("OVERWIEGHT ")

except Exception:
    print("Invalid Input");

print(now.strftime("%Y-%m-%d %H:%M"))
print("\n")
print("Programmed by Pratik Tamhankar")