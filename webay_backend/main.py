import argparse
import json
from search import Search
from listing_editor import ListingEditor
from sort import QuickSort

def parse_args():
    """Return a list of arguments supplied from the command line."""
    parser = argparse.ArgumentParser()  # Create AP object.
    # Construct set of valid arguments.
    parser.add_argument('--search', type=str, help="Search Term")
    parser.add_argument('--sort', action='store_true', help="Sort method")
    parser.add_argument('--create', action='store_true',
                        help="Create new listing.")
    parser.add_argument('--modify', action='store_true',
                        help="Modify existing listing.")
    parser.add_argument('--delete', action='store_true',
                        help="Delete existing listing.")
    parser.add_argument('--print', nargs='?', const=1, type=int,
                        help="Print 10 listings per page, pass integer argument for print select page")
    return parser.parse_args()  # Return parsed arguments.

# Below is the part of main.py that will execute.
if __name__ == "__main__":
    searcher = Search()
    editor = ListingEditor()
    raw_args = parse_args()
    Sorter = QuickSort()
    arg_list = {}

    path_active = "data_files/active_listings.json"
    path_matched = "data_files/matched_listings.json"
    path_sorted = "data_files/price_sorted_listings.json"

    for key in vars(raw_args):  # Key refers to item being detailed by user.
        value = getattr(raw_args, key)  # Value of item, this is users input.
        arg_list[key] = value

    #Check if the argument for print is 0, or an error will occur 
    if arg_list['print'] == 0:
        arg_list['print'] = 1    
    
    if arg_list['search']:
        listings = searcher.load_data(path_active)
        ordered_matches = searcher.search_titles(arg_list['search'], listings)
        print(ordered_matches)
        if ordered_matches:
            editor.safe_write(path_matched,ordered_matches)
            editor.print_listings(path_matched)
        else:
            print("No Listings Match Search Terms")

        sort_option = input("Would you like to sort your listings? Y/N: ")
        if sort_option.lower() == "y":
            Sorter.low_to_high_helper(path_matched)
            editor.print_listings(path_sorted)
        

    if arg_list['create']:
        print("Create a new listing...\n")
        new_title = input("Title: ")
        new_price = int(input("Price: "))
        listings = searcher.load_data(path_active)
        editor.add_listing(path_active, new_title, new_price)
    
    if arg_list['modify']:
        print("Modify an existing listing...\n")
        mod_sku = int(input("SKU of listing to modify: "))
        mod_title = input("Updated title: ")
        mod_price = int(input("Updated price: "))
        editor.modify_listing(path_active, mod_sku, mod_title, mod_price)
    
    if arg_list['delete']:
        print("Delete an existing listing...\n")
        del_sku = int(input("SKU of listing to delete: "))
        editor.delete_listing(path_active, del_sku)

    if arg_list['print']:
        print("Printing Listings...\n")
        #Ensuring that the user's argument is not negative when passed as parameter
        if arg_list['print'] < 0:
            pageNum = arg_list['print'] * -1
        else:
            pageNum = arg_list['print']
        editor.print_listings(path_active, pageNum)

    elif arg_list['sort']:
        print("Sorting Listings...\n")
        sort_method = input("Sort by (l2h or h2l): ")
        if sort_method == "l2h":
            Sorter.low_to_high_helper(path_active)
        elif sort_method == "h2l":
            Sorter.high_to_low_helper(path_active)
        else:
            print("Invalid input. Exiting program.")
        editor.print_listings(path_sorted)


            

        
    
    
