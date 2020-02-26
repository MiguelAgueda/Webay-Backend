import json


class ListingEditor:
    def __init__(self):
        pass

    def add_listing(self, path_to_file, title, price):
        with open(path_to_file, 'w') as file:
            active_listings = json.load(file)  # Get all currently posted listings.
            last_sku = active_listings[-1][0]  # Get sku of last listing.
            active_listings.append([last_sku + 1, title, price])  # Add new listing to end of list.
            json.dump(active_listings, file, separators=( ' , ', ' ]'), indent=2)



