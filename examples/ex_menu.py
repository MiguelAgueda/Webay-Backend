
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
   # print(data)  # Print data to the screen.
        search_price = input(
            "Please enter in a SKU, item name, or price.(If searching by price please enter in a preceeding $).\n")
        ("To return to the main menu enter zero.\n")
        #print(data[int(search_sku)].values())
        #print(Quick_Sort(data))
        save_to_file("data_files/price_sorted_listings.json", Quick_Sort(data))
        #Men
        #u()troubleshoot


def Search_Forums():
    print("Search Forums")


def Review_Pages():
    print("Review Pages")


def Quick_Sort(listings):
    data_size = len(listings)

    if(data_size <= 1):
        return listings

    else:
        piv_listing = listings.pop()
        piv = piv_listing[2]
        numbers_bigger = []
        numbers_smaller = []
        sorted_list = []

        for listing in listings:

            if listing[2] > piv:
                numbers_bigger.append(listing)
            else:
                numbers_smaller.append(listing)

        sorted_list = Quick_Sort(numbers_smaller) + [piv_listing]+ Quick_Sort(numbers_bigger)
    return sorted_list

def save_to_file(pathtofile, datatosave):
    with open(pathtofile, 'w' ) as file :
         json.dump(datatosave, file, separators=( ' , ', ' ] '), indent=2)
         file.close()  # Close file, writing changes.
Menu()
