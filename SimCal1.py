print("Welcome To Ahsan Simple Calculator")

print("==================================")

print("Before The Program Starts, May I Know What's Your Name?")

UserName = input("Name: ")


i = 1
while i == 1:
    print("Hello", UserName, "! Please Choose What Operator Do U Want")
    print("1. + \n2. - \n3. x \n4. / \n5. (^) \n6. %")
    Choose1 = int(input("Your Choice: "))
        
    if Choose1 == 1 :
        Number1 = int(input("First Number: "))
        Number2 = int(input("Second Number: "))
    
        Result = Number1 + Number2
        print(Number1,"+",Number2,"=",Result)
        i = 2

    elif Choose1 == 2:
        Number1 = int(input("First Number: "))
        Number2 = int(input("Second Number: "))
            
        Result = Number1 - Number2
        print(Number1,"-",Number2,"=",Result)
        i = 2
    elif Choose1 == 3:
        Number1 = int(input("First Number: "))
        Number2 = int(input("Second Number: "))
            
        Result = Number1 * Number2
        print(Number1,"x",Number2,"=",Result)
        i = 2    
    elif Choose1 == 4:
        Number1 = int(input("First Number: "))
        Number2 = int(input("Second Number: "))
            
        Result = Number1 / Number2
        print(Number1,"/",Number2,"=",Result)
        i = 2
    elif Choose1 == 5:
        Number1 = int(input("First Number: "))
        Number2 = int(input("Second Number: "))
            
        Result = Number1 ** Number2
        print("(",Number1,"^)",Number2,"=",Result)
        i = 2
    elif Choose1 == 6:
        Number1 = int(input("First Number: "))
        Number2 = int(input("Second Number: "))
            
        Result = Number1 % Number2
        print(Number1,"%",Number2,"=",Result)
        i = 2
    else:
        print("The Operator is not exist yet")
        i = 1

    while i == 2:
        fin = int(input("1 For Yes \n2 For No \n Finish? :"))
        if fin == 1:
            print("Thank You,",UserName,"!")
            i=0
        elif fin == 2:
            i = 1
        else:
            print("Wrong Input \n Getting Restart")
            i = 1

'''
i = 1
while (i<=5):
    print("Hello Looping In Python")
    i+=1
'''

'''
x = 1
for x in range(1,2):
    print("This is for loop")
'''