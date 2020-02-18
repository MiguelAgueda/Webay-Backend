def Menu():
    print("Welcome to Webay. Below are your current options: \n")
    print("1. Browse Webstore:\n")
    print("2. Search forums:\n")
    print("3. View Review pages:\n")
    print("4. Quit the program:\n")

    response = input("What would you like to do?: ")
    response = int(response)
    print (response)
    if (response == 1):
        Browse_WebStore()
    if (response == 2):
        Search_Forums()
    if (response == 3):
        Review_Pages()
    if (response == 4):
        quit()
    # if (response != int()):
    #    Menu() 

def Browse_WebStore():
    print("Browsing webstore")

def Search_Forums():
    print("Browing Forums")

def Review_Pages():
    pass 


