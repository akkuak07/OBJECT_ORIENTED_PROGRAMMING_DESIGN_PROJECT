# About The Project:

FoodApp Project is created Using OOPS concept and MVC(Model View Controller) Architecture on Python. It's an online food ordering system accepts orders from customers and delivers at customer’s address. Items are selected from a menu and the total bill amount is calculated. Selected items may be put in a cart and addition, deletion of items in the cart is possible. Once the order is confirmed, the time taken for delivery is intimated and the order can be tracked. There are several payment modes, cash/wallet/bank transfer/credit/debit card on delivery or pre-paid. Orders placed may be cancelled if delivery time exceeds 10% of specified time.

# Features:
**Authentication:**

* Sign up as new user/Login as existing user.
* Password Authentication and option to reenter password if entered wrong password.
* Option of sign up if user's details are not there in database while logging in.

**Order:**

* Accepts Customer's Location in the form of latitude and longitude coordinates.
* Displays the Restaurants.
* Displays the Menu of the Selected Restaurant which contains columns like Categoy, Item, Ratings and Price.

**Cart:**

* Add/Remove items in/from the cart.
* Add items from cart to the wishlist.
* Discard the Order.
* Displays items in the order.
* Go to payment section.

**Payment:**

* Displays total amount including delivery charges.
* Option to add promocode- Save50 and Save20.
* **Payment options:**
     * UPI
     * Netbanking
     * Credit card
     * Debit card
     
**Tracking:**


* Displays estimated delivery time based on the distance of customer from the restaurant and preparation time of the restaurant.
* Option to cancel the order if delivery time exceeds 10% of estimated delivery time.
* Option to rate the app and food.

# Source files:

**The Project contains 4 files essential Files one each for MVC respectively and one Database file:**
* foodapp.py(Controller file)
* foodappui.py(View File)
* foodappclasses.py(Model file)
* project.db (database file)

**Description:**
* For the program to run properly all the source code and the database files should be in the same directory
* The Driver code is written foodapp.py and other 2 files are imported as modules to this file.
* To execute the program use:- python foodapp.py


# Database Specification:

Database connectivity is done using the sqlite module on local host.

**Database name:** project.db

**Tables :** 
* **user:** Contains user credential specific to the app.
* **Restaurants:** Contains the list of restaurants and their location
* **menu:** Contains the Menu details specific to a particular restaurant.
* **useraccounts:** Contains the credential that mimics the payment gateway functionality. 
		    Only the user that exist in this table will be able to make payment for ordering the food.
	

# Note:

The OS module used in the project is compatiable with with Windows OS, in case the project has to be run 
on the Linux environment then the cls command should be replaced with the clear and sys.exit command can be ommitted.
