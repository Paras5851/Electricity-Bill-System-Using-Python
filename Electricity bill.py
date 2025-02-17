# Program to calculate electricity bill 

# if 500 unit used - pay Rs 5 for each unit
# if 700 unit used - pay Rs 10 for each unit
# if 1000 unit used - pay Rs 15 for each unit
# if more than 1000 unit used - pay Rs 20 for each unit

def electricity_bill(n):
    if n<=500:
        print("Your Bill is Rs",n*5)
    elif n>500 and n<=700:
        print("Your Bill is Rs",n*10)
    elif n>700 and n<=1000:
        print("Your Bill is Rs",n*15)
    elif n>1000:
        print("Your Bill is Rs",n*20)

def instructions():
    print("Instructions:")
    print("*Last date of paying bill is 01-Mar-2025.")
    print('''*After Due date you will need to pay 
Rs.1000 as fine.''')
    print("*Electricity office New Delhi.")

while True:
    print("-"*40)
    print("                  BSES")
    print("-"*40)
    print("Billing Details:")
    a = input("Name of customer: ")
    n = int(input("Unit of Electricity used: "))
    print("-"*40)
    electricity_bill(n)
    print("-"*40)
    instructions()
    print("-"*40)
    print("***************Thank You****************")
    repeat = input("Do you want to print more bills? ")
    if repeat == "no" or repeat == "No":
        break
    