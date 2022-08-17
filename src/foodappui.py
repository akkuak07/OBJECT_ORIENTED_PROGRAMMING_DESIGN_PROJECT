import os
import time
import getpass


def mainmenu():

    os.system('cls')

    print("Welcome To Food App")
    print("Please Select Option from Below")
    print('\t1. Sign Up')
    print('\t2. Login')
    print('\t3. Exit')

    selection = int(input("\tSelection:"))
    if selection not in [1, 2, 3]:
        print("Invalid Input. Please Try again")
        time.sleep(1)
        mainmenu()

    return selection


def signupmenu():

    os.system('cls')

    print("*****Signup Page*****")

    name = input("Please enter name:")
    email = input("Please enter email:")
    mobno = input("Please enter Mobno:")
    password = getpass.getpass()

    while True:
        if '@' in email and '.com' in email:
            break
        else:
            email = input('Please enter a valid email address: ')

    while True:
        if len(mobno) == 10:
            break
        else:
            mobno = input('Please enter a valid phone number: ')

    return [email, password, int(mobno), name]


def loginmenu():

    os.system('cls')
    print("*****Login Page*****")
    email = input("Please enter email:")
    password = getpass.getpass()
    return [email, password]


def exitmsg():

    print("Thanks for Using our App. Goodbye")
    time.sleep(1)


def alreadyexists():

    print("Email already in use. Please try again")
    time.sleep(1)


def welcomemsg(name):

    print("Welcome to App "+name+"!")
    time.sleep(1)


def invaliddata():

    print("Incorrect Credentials. Please try again")
    time.sleep(1)


def showrestaurants(rdetails):

    os.system('cls')
    print('Please select from the following  restaurants')
    for row in rdetails:
        print(str(row[0]) + ".\t" + row[1] + "\t", row[4])
    option = input("Selection:")

    if option.isnumeric() and int(option) < len(rdetails):
        return option
    else:
        print("Invalid Input. Please try again")
        time.sleep(1)
        showrestaurants()


def showmenu(mdetails, eta):

    os.system('cls')
    foodict = dict()
    while (True):
        os.system('cls')
        print('Please select from the following Menu')
        print('Fid\tFood Item\tprice')
        for row in mdetails:
            print(str(row[0]) + ".\t" + row[2] + ".\t" + str(row[3]))
        print("ETA from the selected restaurant:", eta, "Mins")
        fooditem = input("FoodItem:")
        qty = input("Quantity:")

        if fooditem.isnumeric() and int(fooditem) <= int(mdetails[-1][0]) and int(fooditem) >= int(mdetails[0][0]):
            item = [mdetails[idx]
                    for idx in range(len(mdetails)) if mdetails[idx][0] == int(fooditem)]

            foodict[fooditem] = [item[0][2], item[0][3], qty]
            print("Item Added:-", foodict[fooditem][0], "Price:-",
                  foodict[fooditem][1], "Quantity:-", foodict[fooditem][2])
        else:
            print("Invalid Input. Please try again")
            time.sleep(1)

        print("Do you want to add more items? Y/N")
        check = input()
        if check == 'N' or check == 'n':
            break

    os.system('cls')
    print("Contents of your Cart as Follows:")
    print("Fid\tFoodname\tprice\tqty")
    for key, values in foodict.items():
        print(key, values[0], values[1], values[2])

    while(True):
        print("Do you want to delete any items?Y/N")
        check = input()
        if check == 'N' or check == 'n':
            break
        delitm = input("item No to Delete:")
        foodict.pop(delitm)

    os.system('cls')
    print("Final Contents of your Cart as Follows:")
    print("Foodname\tprice\tqty")
    for key, values in foodict.items():
        print(values[0], values[1], values[2])

    print("Do you to Procced with the cart(y) or discard and Goto Main Menu(n)?")
    flag = input()
    if flag == 'N' or flag == 'n':
        edict = dict()
        return edict

    return foodict


def amountless():
    print("Amount Must be more than Rs 100 for ordering")
    print("Please retry")
    time.sleep(1)


def showbill(amount, deliverychg, couponstatus):
    os.system('cls')
    print("Amount for items on your food cart: Rs", amount)
    print("Delivery Charges: Rs", deliverychg)

    couponl = list()
    if couponstatus[0] == 1:
        couponl.append('save50')
    if couponstatus[1] == 1:
        couponl.append('save20')

    df = 1

    if len(couponl) == 0:
        print("No coupons available to apply")
        print("You will be taken to payment Gateway")
        time.sleep(2)

    else:
        print("Please select from the avaiable coupon")
        for i, coupon in enumerate(couponl):
            print(coupon)
        option = input("Enter Coupon Code:")
        if option == "save50":
            df = 0.5
            print(" save50 Applied")

        if option == "save20":
            df = 0.8
            print(" save20 Applied")
        print("You will be taken to payment Gateway")
        time.sleep(2)

    return df


def paymentmethod(tamount):
    os.system('cls')
    print("Please Select a payment Mode for the payment of cart value:", tamount)
    print('\t1. UPI')
    print('\t2. NetBanking')
    print('\t3. DebitCard')
    print('\t4. CreditCard')
    option = input("Selection:")

    if(option == "1"):
        cred = input("Please enter your mobile Number:")
    elif(option == "2"):
        cred = input("Please enter your EMAIL:")
    elif(option == "3"):
        cred = input("Please enter your DebitCardNumber:")
    elif(option == "4"):
        cred = input("Please enter your CreditCard Number:")
    else:
        print("Invalid Input. Please try again.")
        paymentmethod(tamount)

    pin = getpass.getpass()

    return [option, cred, pin]


def paymentdone():

    print("Payment Successful")
    print("Your food is on the way")
