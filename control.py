condition = True
name = "Roger"
if condition == True:
    print("The condition")
    print("was True")
elif name == "Roger":
    print("Hello Roger")
elif name == "Syd":
    print("Hello Syd")
elif name == "Flavio":
    print("Hello Flavio")
else:
    print("The condition")
    print("was False")

#using multiple if statement

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
    
if age >= 18 and age < 65:
    print("You are an adult.")
    
if age >= 65:
    print("You are a senior citizen.")


#nested conditions

print("Welcome to the Paintball Park")
height = int(input("What is your height in cm?"))

bill = 0

if height >= 100:
    print("You can play paintball")
    age = int(input("What is your age: "))
    if age < 12:
        bill = 5
        print("Child tickets are 5$")
    elif age < 18:
        bill = 9
        print("Teenage tickets are 9$")
    else:
        bill = 12
        print("You will Pay 12$ as an Adult ")
    
    takePicture = input("Do you want a picture taken? Y or N. ")
    if takePicture == "Y":
        bill += 3
        
    print(f"Your Total bill is {bill}")   
else:
    print("Access denied, you need to meet minimum height") 
