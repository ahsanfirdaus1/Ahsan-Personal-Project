import getpass
import random

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("------------Welcome To Daihatsu Car Dealer--------------")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
Transaction = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
NumTrac = random.randint(0,20)
i = 1
while i == 1:
        print("Before We Continue, Please Input Your Information Below!")
        User = input("Name: ")
        Age = int(input("Age: "))
        if Age <=17:
            print("Sorry, You Can't Purchase A Car.\nYou Can Buy It With Your Parrent")
            i = 1
        else:
            print("Hello",User)

            print()
            print("Car List: ")
            print("----------")
            print("1. LCGC")
            print("2. MPV")
            print("3. SUV")

            i = 2
            while i == 2:
                Cho1 = input("Your Choice: ")
                if Cho1 == "lcgc" or Cho1 == "LCGC" or Cho1 == "1":
                    print("Your Choice is LCGC")
                    print("Here's The List: ")
                    print("1. Ayla ")
                    print("2. Sirion")

                    i = 3
                    while i == 3:
                        Cho2 = input("Your Choice: ")
                        if Cho2 == "ayla" or Cho1 == "AYLA" or Cho1 == "1":
                            print("Your Choice is Ayla, Mr.",User)
                            print("The Price is About: Rp 100 juta")
                            print("Do You Want To Continue This Transaction?\n 1. Yes 2. No")

                            i = 4
                            while i == 4:
                                Cho3 = input("Continue? ")
                                if Cho3 == "Yes" or Cho3 == "YES" or Cho3 == "yes" or Cho3 == "1":
                                    print("Payment Method Available: ")
                                    print("1. Debit Card \n2. Credit Card")

                                    i = 5 
                                    while i == 5:
                                        Cho4 = input("Your Payment Method: ")

                                        if Cho4 == "1" or Cho4 == "DC" or Cho4 == "Dedit Card" or Cho4 == "Debit card" or Cho4 == "DEBIT CARD":
                                            print("Your Payment Method is Debit Card")
                                            CNum = int(input("Input Your Card Number: "))
                                            CardPass = getpass.getpass(prompt="Your Password: ")
                                            print("Waiting For The Process....")
                                            print("")
                                            print("..")
                                            print("...")
                                            print("....")
                                            print(".....")
                                            print("Payment Sucess! :)")
                                            print("Your Name: ",User)
                                            print("Your Age: ",Age)
                                            print("Transaction Number: ", NumTrac)
                                            print("Thank You", User)
                                            i = 1000

                                        elif Cho4 == "2" or Cho4 == "CC" or Cho4 == "Credit Card" or Cho4 == "credit card" or Cho4 == "CREDIT CARD":
                                            print("Your Payment Method is Credit Card")
                                            CNum = int(input("Input Your Card Number: "))
                                            CardPass = getpass.getpass(prompt="Your Password: ")
                                            print("Waiting For The Process....")
                                            print("")
                                            print("..")
                                            print("...")
                                            print("....")
                                            print(".....")
                                            print("Payment Sucess! :)")
                                            print("Your Name: ",User)
                                            print("Your Age: ",Age)
                                            print("Transaction Number: ", NumTrac)
                                            print("Thank You", User)
                                            i = 1000
                                        else: 
                                            print("Invalid Choice")
                                            i = 5

                                else: 
                                    print("Okay Good Bye", User)
                                    i = 1

                        
                        elif Cho2 == "sirion" or Cho1 == "SIRION" or Cho1 == "2":
                            print("Your Choice is Sirion, Mr.",User)
                            print("The Price is About: Rp 200 juta")
                            print("Do You Want To Continue This Transaction?\n 1. Yes 2. No")

                            i = 4
                            while i == 4:
                                Cho3 = input("Continue? ")
                                if Cho3 == "Yes" or Cho3 == "YES" or Cho3 == "yes" or Cho3 == "1":
                                    print("Payment Method Available: ")
                                    print("1. Debit Card \n2. Credit Card")

                                    i = 5 
                                    while i == 5:
                                        Cho4 = input("Your Payment Method: ")

                                        if Cho4 == "1" or Cho4 == "DC" or Cho4 == "Dedit Card" or Cho4 == "Debit card" or Cho4 == "DEBIT CARD":
                                            print("Your Payment Method is Debit Card")
                                            CNum = int(input("Input Your Card Number: "))
                                            CardPass = getpass.getpass(prompt="Your Password: ")
                                            print("Waiting For The Process....")
                                            print("")
                                            print("..")
                                            print("...")
                                            print("....")
                                            print(".....")
                                            print("Payment Sucess! :)")
                                            print("Your Name: ",User)
                                            print("Your Age: ",Age)
                                            print("Transaction Number: ", NumTrac)
                                            print("Thank You", User)
                                            i = 1000

                                        elif Cho4 == "2" or Cho4 == "CC" or Cho4 == "Credit Card" or Cho4 == "credit card" or Cho4 == "CREDIT CARD":
                                            print("Your Payment Method is Credit Card")
                                            CNum = int(input("Input Your Card Number: "))
                                            CardPass = getpass.getpass(prompt="Your Password: ")
                                            print("Waiting For The Process....")
                                            print("")
                                            print("..")
                                            print("...")
                                            print("....")
                                            print(".....")
                                            print("Payment Sucess! :)")
                                            print("Your Name: ",User)
                                            print("Your Age: ",Age)
                                            print("Transaction Number: ", NumTrac)
                                            print("Thank You", User)
                                            i = 1000
                                        else: 
                                            print("Invalid Choice")
                                            i = 5

                                else: 
                                    print("Okay Good Bye", User)
                                    i = 1
                        else: 
                            print("Sorry Sir, Your Input Is Invalid")
                            i = 3

                elif Cho1 == "mpv" or Cho1 == "MPV" or Cho1 == "2":
                    print("Your Choice is MPV")
                    print("Here's The List: ")
                    print("1. Xenia")
                    print("2. Sigra")
                    print("3. Luxio")
                    print("4. Gran Max")
                    
                    i = 3
                    while i == 3:
                        Cho2 = input("Your Choice: ")
                        if Cho2 == "xenia" or Cho1 == "XENIA" or Cho1 == "1":
                            print("Your Choice is Xenia, Mr.",User)
                            print("The Price is About: Rp 180 juta")
                            print("Do You Want To Continue This Transaction?\n 1. Yes 2. No")

                            i = 4
                            while i == 4:
                                Cho3 = input("Continue? ")
                                if Cho3 == "Yes" or Cho3 == "YES" or Cho3 == "yes" or Cho3 == "1":
                                    print("Payment Method Available: ")
                                    print("1. Debit Card \n2. Credit Card")

                                    i = 5 
                                    while i == 5:
                                        Cho4 = input("Your Payment Method: ")

                                        if Cho4 == "1" or Cho4 == "DC" or Cho4 == "Dedit Card" or Cho4 == "Debit card" or Cho4 == "DEBIT CARD":
                                            print("Your Payment Method is Debit Card")
                                            CNum = int(input("Input Your Card Number: "))
                                            CardPass = getpass.getpass(prompt="Your Password: ")
                                            print("Waiting For The Process....")
                                            print("")
                                            print("..")
                                            print("...")
                                            print("....")
                                            print(".....")
                                            print("Payment Sucess! :)")
                                            print("Your Name: ",User)
                                            print("Your Age: ",Age)
                                            print("Transaction Number: ", NumTrac)
                                            print("Thank You", User)
                                            i = 1000

                                        elif Cho4 == "2" or Cho4 == "CC" or Cho4 == "Credit Card" or Cho4 == "credit card" or Cho4 == "CREDIT CARD":
                                            print("Your Payment Method is Credit Card")
                                            CNum = int(input("Input Your Card Number: "))
                                            CardPass = getpass.getpass(prompt="Your Password: ")
                                            print("Waiting For The Process....")
                                            print("")
                                            print("..")
                                            print("...")
                                            print("....")
                                            print(".....")
                                            print("Payment Sucess! :)")
                                            print("Your Name: ",User)
                                            print("Your Age: ",Age)
                                            print("Transaction Number: ", NumTrac)
                                            print("Thank You", User)
                                            i = 1000
                                        else: 
                                            print("Invalid Choice")
                                            i = 5

                                else: 
                                    print("Okay Good Bye", User)
                                    i = 1
                        
                        elif Cho2 == "sigra" or Cho1 == "SIGRA" or Cho1 == "2":
                            print("Your Choice is Sigra, Mr.",User)
                            print("The Price is About: Rp 120 juta")
                            print("Do You Want To Continue This Transaction?\n 1. Yes 2. No")

                            i = 4
                            while i == 4:
                                Cho3 = input("Continue? ")
                                if Cho3 == "Yes" or Cho3 == "YES" or Cho3 == "yes" or Cho3 == "1":
                                    print("Payment Method Available: ")
                                    print("1. Debit Card \n2. Credit Card")

                                    i = 5 
                                    while i == 5:
                                        Cho4 = input("Your Payment Method: ")

                                        if Cho4 == "1" or Cho4 == "DC" or Cho4 == "Dedit Card" or Cho4 == "Debit card" or Cho4 == "DEBIT CARD":
                                            print("Your Payment Method is Debit Card")
                                            CNum = int(input("Input Your Card Number: "))
                                            CardPass = getpass.getpass(prompt="Your Password: ")
                                            print("Waiting For The Process....")
                                            print("")
                                            print("..")
                                            print("...")
                                            print("....")
                                            print(".....")
                                            print("Payment Sucess! :)")
                                            print("Your Name: ",User)
                                            print("Your Age: ",Age)
                                            print("Transaction Number: ", NumTrac)
                                            print("Thank You", User)
                                            i = 1000

                                        elif Cho4 == "2" or Cho4 == "CC" or Cho4 == "Credit Card" or Cho4 == "credit card" or Cho4 == "CREDIT CARD":
                                            print("Your Payment Method is Credit Card")
                                            CNum = int(input("Input Your Card Number: "))
                                            CardPass = getpass.getpass(prompt="Your Password: ")
                                            print("Waiting For The Process....")
                                            print("")
                                            print("..")
                                            print("...")
                                            print("....")
                                            print(".....")
                                            print("Payment Sucess! :)")
                                            print("Your Name: ",User)
                                            print("Your Age: ",Age)
                                            print("Transaction Number: ", NumTrac)
                                            print("Thank You", User)
                                            i = 1000
                                        else: 
                                            print("Invalid Choice")
                                            i = 5

                                else: 
                                    print("Okay Good Bye", User)
                                    i = 1

                        elif Cho2 == "luxio" or Cho1 == "LUXIO" or Cho1 == "3":
                            print("Your Choice is Luxio, Mr.",User)
                            print("The Price is About: Rp 190 juta")
                            print("Do You Want To Continue This Transaction?\n 1. Yes 2. No")

                            i = 4
                            while i == 4:
                                Cho3 = input("Continue? ")
                                if Cho3 == "Yes" or Cho3 == "YES" or Cho3 == "yes" or Cho3 == "1":
                                    print("Payment Method Available: ")
                                    print("1. Debit Card \n2. Credit Card")

                                    i = 5 
                                    while i == 5:
                                        Cho4 = input("Your Payment Method: ")

                                        if Cho4 == "1" or Cho4 == "DC" or Cho4 == "Dedit Card" or Cho4 == "Debit card" or Cho4 == "DEBIT CARD":
                                            print("Your Payment Method is Debit Card")
                                            CNum = int(input("Input Your Card Number: "))
                                            CardPass = getpass.getpass(prompt="Your Password: ")
                                            print("Waiting For The Process....")
                                            print("")
                                            print("..")
                                            print("...")
                                            print("....")
                                            print(".....")
                                            print("Payment Sucess! :)")
                                            print("Your Name: ",User)
                                            print("Your Age: ",Age)
                                            print("Transaction Number: ", NumTrac)
                                            print("Thank You", User)
                                            i = 1000

                                        elif Cho4 == "2" or Cho4 == "CC" or Cho4 == "Credit Card" or Cho4 == "credit card" or Cho4 == "CREDIT CARD":
                                            print("Your Payment Method is Credit Card")
                                            CNum = int(input("Input Your Card Number: "))
                                            CardPass = getpass.getpass(prompt="Your Password: ")
                                            print("Waiting For The Process....")
                                            print("")
                                            print("..")
                                            print("...")
                                            print("....")
                                            print(".....")
                                            print("Payment Sucess! :)")
                                            print("Your Name: ",User)
                                            print("Your Age: ",Age)
                                            print("Transaction Number: ", NumTrac)
                                            print("Thank You", User)
                                            i = 1000
                                        else: 
                                            print("Invalid Choice")
                                            i = 5

                                else: 
                                    print("Okay Good Bye", User)
                                    i = 1
                        elif Cho2 == "gran max" or Cho1 == "GRAN MAX" or Cho1 == "4":
                            print("Your Choice is Gran Max, Mr.",User)
                            print("The Price is About: Rp 160 juta")
                            print("Do You Want To Continue This Transaction?\n 1. Yes 2. No")

                            i = 4
                            while i == 4:
                                Cho3 = input("Continue? ")
                                if Cho3 == "Yes" or Cho3 == "YES" or Cho3 == "yes" or Cho3 == "1":
                                    print("Payment Method Available: ")
                                    print("1. Debit Card \n2. Credit Card")

                                    i = 5 
                                    while i == 5:
                                        Cho4 = input("Your Payment Method: ")

                                        if Cho4 == "1" or Cho4 == "DC" or Cho4 == "Dedit Card" or Cho4 == "Debit card" or Cho4 == "DEBIT CARD":
                                            print("Your Payment Method is Debit Card")
                                            CNum = int(input("Input Your Card Number: "))
                                            CardPass = getpass.getpass(prompt="Your Password: ")
                                            print("Waiting For The Process....")
                                            print("")
                                            print("..")
                                            print("...")
                                            print("....")
                                            print(".....")
                                            print("Payment Sucess! :)")
                                            print("Your Name: ",User)
                                            print("Your Age: ",Age)
                                            print("Transaction Number: ", NumTrac)
                                            print("Thank You", User)
                                            i = 1000

                                        elif Cho4 == "2" or Cho4 == "CC" or Cho4 == "Credit Card" or Cho4 == "credit card" or Cho4 == "CREDIT CARD":
                                            print("Your Payment Method is Credit Card")
                                            CNum = int(input("Input Your Card Number: "))
                                            CardPass = getpass.getpass(prompt="Your Password: ")
                                            print("Waiting For The Process....")
                                            print("")
                                            print("..")
                                            print("...")
                                            print("....")
                                            print(".....")
                                            print("Payment Sucess! :)")
                                            print("Your Name: ",User)
                                            print("Your Age: ",Age)
                                            print("Transaction Number: ", NumTrac)
                                            print("Thank You", User)
                                            i = 1000
                                        else: 
                                            print("Invalid Choice")
                                            i = 5

                                else: 
                                    print("Okay Good Bye", User)
                                    i = 1
                        else: 
                            print("Sorry Sir, Your Input Is Invalid")
                            i = 3

                elif Cho1 == "suv" or Cho1 == "SUV" or Cho1 == "3":
                    print("Your Choice is SUV")
                    print("Here's The List: ")
                    print("1. Terios")

                    i = 3
                    while i == 3:
                        Cho2 = input("Your Choice: ")
                        if Cho2 == "terios" or Cho1 == "TERIOS" or Cho1 == "1":
                            print("Your Choice is Terios, Mr.",User)
                            print("The Price is About: Rp 200 juta")
                            print("Do You Want To Continue This Transaction?\n 1. Yes 2. No")

                            i = 4
                            while i == 4:
                                Cho3 = input("Continue? ")
                                if Cho3 == "Yes" or Cho3 == "YES" or Cho3 == "yes" or Cho3 == "1":
                                    print("Payment Method Available: ")
                                    print("1. Debit Card \n2. Credit Card")

                                    i = 5 
                                    while i == 5:
                                        Cho4 = input("Your Payment Method: ")

                                        if Cho4 == "1" or Cho4 == "DC" or Cho4 == "Dedit Card" or Cho4 == "Debit card" or Cho4 == "DEBIT CARD":
                                            print("Your Payment Method is Debit Card")
                                            CNum = int(input("Input Your Card Number: "))
                                            CardPass = getpass.getpass(prompt="Your Password: ")
                                            print("Waiting For The Process....")
                                            print("")
                                            print("..")
                                            print("...")
                                            print("....")
                                            print(".....")
                                            print("Payment Sucess! :)")
                                            print("Your Name: ",User)
                                            print("Your Age: ",Age)
                                            print("Transaction Number: ", NumTrac)
                                            print("Thank You", User)
                                            i = 1000

                                        elif Cho4 == "2" or Cho4 == "CC" or Cho4 == "Credit Card" or Cho4 == "credit card" or Cho4 == "CREDIT CARD":
                                            print("Your Payment Method is Credit Card")
                                            CNum = int(input("Input Your Card Number: "))
                                            CardPass = getpass.getpass(prompt="Your Password: ")
                                            print("Waiting For The Process....")
                                            print("")
                                            print("..")
                                            print("...")
                                            print("....")
                                            print(".....")
                                            print("Payment Sucess! :)")
                                            print("Your Name: ",User)
                                            print("Your Age: ",Age)
                                            print("Transaction Number: ", NumTrac)
                                            print("Thank You", User)
                                            i = 1000
                                        else: 
                                            print("Invalid Choice")
                                            i = 5

                                else: 
                                    print("Okay Good Bye", User)
                                    i = 1
                        else:
                            print("Sorry Sir, Your Input Is Invalid")
                            i = 3

                else:
                    print("Sorry Your Input Is Not Found Yet!") 
                    i = 2
                    

