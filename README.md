FOODAPP

FoodApp Project is created Using OOPS concept and MVC(Model View Controller) Architecture on Python.

The Project contains 4 files essential Files one each for MVC respectively and one Database file:-
i) foodapp.py(Controller file)
ii) foodappui.py(View File)
iii) foodappclasses.py(Model file)
iv) project.db (database file)

-> For the program to run properly all the source code and the database files should be in the same directory
-> The Driver code is written foodapp.py and other 2 files are imported as modules to this file.
-> To execute the program use:- python foodapp.py

DATABASE SPECIFICATION:-

Database connectivity is done using the sqlite module on local host.
Database name:- project.db
Tables :- 
i)   user:- Contains user credential specific to the app.
ii)  Restaurants:- Contains the list of restaurants and their location
iii) menu :- Contains the Menu details specific to a particular restaurant.
iv)  useraccounts:-Contains the credential that mimics the payment gateway functionality. 
		   Only the user that exist in this table will be able to make payment for ordering the food.
	

Note:- The OS module used in the project is compatiable with with Windows OS, in case the project has to be run 
on the Linux environment then the cls command should be replaced with the clear and sys.exit command can be ommitted.