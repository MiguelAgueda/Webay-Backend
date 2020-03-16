import json
import sys
from math import ceil

class ListingEditor:
    def __init__(self):
        pass

    def safe_read(self, path_to_file):
        """Safely load and return data from a specified JSON file."""
        try:
            with open(path_to_file, 'r') as file:
                return_data = json.load(file)
                file.close()
                return return_data
        except:
            print("File not found. Check if the file at " + path_to_file + 
                  " exists, or if you are in the correct directory of /webay when accessing this program")
            sys.exit(1)
        

    def safe_write(self, path_to_file, data_to_write):
        """Safely write data to a specified JSON file."""
        with open(path_to_file, 'w') as file:
            json.dump(data_to_write, file,
                      separators=(' , ', ' ] '), indent=2)
            file.close()

    def add_listing(self, path_to_file, title, price):
        """Add listing to data stored on specified path."""
        # Get all currently posted listings.
        active_listings = self.safe_read(path_to_file)
        last_sku = active_listings[-1][0]  # Get sku of last listing.
        # Create a safe copy of active listings to write to.
        # Add new listing to end of list.
        active_listings.append([last_sku + 1, title, price])
        # Save listings to file.
        self.safe_write(path_to_file, active_listings)

    def modify_listing(self, path_to_file, target_sku, title, price):
        """Edit specified listing stored on specified path."""
        active_listings = self.safe_read(path_to_file)
        for listing in active_listings:
            if listing[0] == target_sku:  # If listing to edit is found.
                listing[1] = title  # Edit title.
                listing[2] = price  # Edit price.
                break

        self.safe_write(path_to_file, active_listings)

    def delete_listing(self, path_to_file, target_sku):
        """Delete an existing listing with target SKU on specified file."""
        active_listings = self.safe_read(path_to_file)
        for index, listing in enumerate(active_listings):
            # If the listing to delete is found.
            if listing[0] == target_sku:
                del active_listings[index]  # Delete the listing.
                break

        self.safe_write(path_to_file, active_listings)

    def print_listings(self, path_to_file, user_page_number=1):       #When called, an argument for user_page_number is not needed as it is 1 by default
        """Format and print first ten listings from a specified file."""
        active_listings = self.safe_read(path_to_file)
        itemsPerPage = 10
        totalPages = ceil((len(active_listings)-1)/itemsPerPage)
        
        #Prevent user from placing too big of a page number as an argument
        if user_page_number > totalPages:
            user_page_number = totalPages

        firstListing = user_page_number * itemsPerPage - itemsPerPage
        lastListing = user_page_number * itemsPerPage
        for listing in active_listings[firstListing:lastListing]:
            print(F"SKU: {listing[0]}\tTitle: {listing[1]}\tPrice: {listing[2]}")
        
        print("\nPage " + str(user_page_number) + " of " + str(totalPages))
        
