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
    print("Browse webstore")

def Search_Forums():
    print("Search Forums")

def Review_Pages():
    print("Review Pages")

Menu()
