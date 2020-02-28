import json


class ListingEditor:
    def __init__(self):
        pass

    def __safe_read(self, path_to_file):
        with open(path_to_file, 'r') as file:
            return_data = json.load(file)
            file.close()
            return return_data

    def __safe_write(self, path_to_file, data_to_write):
        with open(path_to_file, 'w') as file:
            json.dump(data_to_write, file,
                      separators=(' , ', ' ] '), indent=2)
            file.close()

    def add_listing(self, path_to_file, title, price):
        """Add listing to data stored on specified path."""
        # Get all currently posted listings.
        active_listings = self.__safe_read(path_to_file)
        last_sku = active_listings[-1][0]  # Get sku of last listing.
        # Create a safe copy of active listings to write to.
        # Add new listing to end of list.
        active_listings.append([last_sku + 1, title, price])
        # Save listings to file.
        self.__safe_write(path_to_file, active_listings)

    def modify_listing(self, path_to_file, target_sku, title, price):
        """Edit specified listing stored on specified path."""
        active_listings = self.__safe_read(path_to_file)
        for listing in active_listings:
            if listing[0] == target_sku:  # If listing to edit is found.
                listing[1] = title  # Edit title.
                listing[2] = price  # Edit price.
                break

        self.__safe_write(path_to_file, active_listings)

    def delete_listing(self, path_to_file, target_sku):
        active_listings = self.__safe_read(path_to_file)
        for index, listing in enumerate(active_listings):
            # If the listing to delete is found.
            if listing[0] == target_sku:
                del active_listings[index]  # Delete the listing.
                break

        self.__safe_write(path_to_file, active_listings)

    def print_listings(self, path_to_file):
        active_listings = self.__safe_read(path_to_file)
        for listing in active_listings:
            print(F"\nTitle:\t{listing[1]}\nPrice:\t{listing[2]}\n\n")
