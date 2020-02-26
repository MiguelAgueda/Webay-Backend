   
import json
import random


file_path = "data_files/sample_listings.json"  # Path to data file.

def Menu():
    print("Welcome to Webay. Below are your current options: \n")
    print("1. Browse Webstore:\n")
    print("2. Search forums:\n")
    print("3. View Review pages:\n")
    print("4. Quit the program:\n")

    response = input("What would you like to do?: ")
    print(response)

    if (response == '1'):
        Browse_WebStore()
    elif (response == '2'):
        Search_Forums()
    elif (response == '3'):
        Review_Pages()
    elif (response == '4'):
        quit()
    else:
        print("Invalid Input")
        Menu()

def Browse_WebStore():
    with open(file_path, 'r') as file:  # Open file in read-only mode.
        data = json.load(file)  # Load data from file.
   #print(data)  # Print data to the screen.
        search_sku = input("Please enter in a SKU, item name, or price.(If searching by price please enter in a preceeding $).\n")
        ("To return to the main menu enter zero.\n")
        print(data[int (search_sku)].values())
        Menu()

def Search_Forums():
    print("Search Forums")

def Review_Pages():
    print("Review Pages")

def Quick_Sort(data):
    data_size = len(data)
    
    if(data_size <= 1):
        return data
    
    else:
 #       piv = data[-1].value(price)

    #numbers_bigger = []
    #numbers_smaller = []

        for items in data:
            print (items)
        #if item > piv:
           # numbers_bigger.append(items)
       # else:
           #numbers_smaller.append(items)
    
    #return Quick_Sort(numbers_bigger) + (piv) + Quick_Sort(numbers_bigger)

Menu()
