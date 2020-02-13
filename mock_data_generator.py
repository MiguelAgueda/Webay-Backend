"""
Source: https://docs.python.org/3.7/tutorial/inputoutput.html#reading-and-writing-files
This program will generate the mock data used by our store's backend.
"""
import json
import random


file_path = "data_files/sample_listings.json"  # Path to data file.
conditions = ["New", "Used", "Like-New"]
sizes = ["Extra Small", "Small", "Medium", "Large", "Extra Large"]
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet",
          "Pink", "Baby Blue", "Fuscia", "Lime Green", "Gray", "Black",
          "Brown", "Tan", "Navy Blue", "Army Green", "Marine Blue",
          "White", "Maroon"]

articles = ["Hat", "Shirt", "Gloves", "Belt", "Pants", "Shorts",
            "Underwear", "Socks"]

def title_generator():
    """Return a randomly composed title."""
    condition = random.choice(conditions)  # Return a random condition from conditions list.
    size = random.choice(sizes)  # Return a random size from sizes list.
    color = random.choice(colors)  # Return a random color from colors list.
    article = random.choice(articles)  # Return a random article from articles list.
    return(f"{condition} {size} {color} {article}")  # Format title in semantic order.

def price_generator():
    """Return a random price between two set price points."""
    dollars = random.randint(0, 49)  # Dollars: random int between 0 - 49
    cents = random.randint(10, 99)  # Cents: random int between 10 - 99
    return(dollars + (cents/100))  # Format price as decimal.


with open(file_path, 'w') as file:  # Open file in write-only mode.
    data_to_store = []  # Initialize an empty list to hold all listings.
    for i in range(1500):  # Create n listings.
        temp_dict = {  # Create a temporary dictionary, filling with listing info.
            "SKU": i,  # Stock Keeping Unit == Listing number.
            "Title": title_generator(),  # Listing title.
            "Price": price_generator()  # Item price.
        }
        data_to_store.append(temp_dict)  # After filling dict, append to a list of listings.
    
    json.dump(data_to_store, file, separators=(' , ', ' : '), indent=4)  # Write list to json file.
    file.close()  # Close file, writing changes.

with open(file_path, 'r') as file:  # Open file in read-only mode.
    data = json.load(file)  # Load data from file.
    print(data)  # Print data to the screen.
