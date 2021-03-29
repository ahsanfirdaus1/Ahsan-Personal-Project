print("Welcome To Ahsan Simple Calculator")

print("==================================")

print("Before The Program Starts, May I Know What's Your Name?")

UserName = input("Name: ")

print("Hello", UserName, "! Please Choose What Operator Do U Want")

print("1. + \n2. - \n3. x \n4. / \n5. (^) \n6. %")

Choose1 = int(input("Your Choice: "))



if Choose1 == 1 :
    Number1 = int(input("First Number: "))
    Number2 = int(input("Second Number: "))
    
    Result = Number1 + Number2
    print(Number1,"+",Number2,"=",Result)
elif Choose1 == 2:
    Number1 = int(input("First Number: "))
    Number2 = int(input("Second Number: "))
    
    Result = Number1 - Number2
    print(Number1,"-",Number2,"=",Result)
elif Choose1 == 3:
    Number1 = int(input("First Number: "))
    Number2 = int(input("Second Number: "))
    
    Result = Number1 * Number2
    print(Number1,"x",Number2,"=",Result)    
elif Choose1 == 4:
    Number1 = int(input("First Number: "))
    Number2 = int(input("Second Number: "))
    
    Result = Number1 / Number2
    print(Number1,"/",Number2,"=",Result)
elif Choose1 == 5:
    Number1 = int(input("First Number: "))
    Number2 = int(input("Second Number: "))
    
    Result = Number1 ** Number2
    print("(",Number1,"^)",Number2,"=",Result)
elif Choose1 == 6:
    Number1 = int(input("First Number: "))
    Number2 = int(input("Second Number: "))
    
    Result = Number1 % Number2
    print(Number1,"%",Number2,"=",Result)
else:
    print("The Operator is not exist yet")
    
