import argparse
import json
from webay_backend.search import Search  # Import Search class from search.py.


def parse_args():
    """Return a list of arguments supplied from the command line."""
    parser = argparse.ArgumentParser()  # Create AP object.
    # Construct set of valid arguments.
    parser.add_argument('--search', type=str, help="Search Term")
    parser.add_argument('--sort', type=str, help="Sort method")
    parser.add_argument('--create', action='store_true',
                        help="Create new listing.")
    parser.add_argument('--modify', action='store_true',
                        help="Modify existing listing.")
    parser.add_argument('--delete', action='store_true',
                        help="Delete existing listing.")
    parser.add_argument('--print', action='store_true',
                        help="Print first 50 listings.")
    return(parser.parse_args())  # Return parsed arguments.


if __name__ == "__main__":
    searcher = Search()
    raw_args = parse_args()
    arg_list = {}

    for key in vars(raw_args):  # Key refers to item being detailed by user.
        value = getattr(raw_args, key)  # Value of item, this is users input.
        arg_list[key] = value

    if arg_list['search']:
        list_of_listings = searcher.load_data('data_files/sample_listings.json')
        ordered_matches = searcher.search_titles(arg_list['search'],
                                                 list_of_listings)
        with open('data_files/ex_matched_listings.json', 'w') as file:
            json.dump(ordered_matches, file, separators=( ' , ', ' ] '), indent=2)
            file.close()
