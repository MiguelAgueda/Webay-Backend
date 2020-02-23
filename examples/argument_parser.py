"""
Source: https://docs.python.org/3/library/argparse.html

This program accepts various commandline arguments and prints the data to 
the user. This can help understand how to handle argument calls for functions.

Usage: python3 argument_parser.py --search="Clothes Line" --add --modify
"""

import argparse


parser = argparse.ArgumentParser()  # Create AP object.
# Below, the parser is used to create a set of valid arguments.
parser.add_argument('--search', type=str, help="Search Term")
parser.add_argument('--sort', type=str, help="Sort method")
parser.add_argument('--create', action='store_true', help="Create new listing.")
parser.add_argument('--modify', action='store_true', help="Modify existing listing.")
parser.add_argument('--delete', action='store_true', help="Delete existing listing.")
parser.add_argument('--print', action='store_true', help="Print first 50 listings.")

argument_list = parser.parse_args()  # Parse command line arguments.

for key in vars(argument_list):  # Key refers to item being detailed by user.
    value = getattr(argument_list, key)  # Value of item, this is users input.
    if value:  # If the user detailed the value for the item,
        print(key + ": " + str(value))  # Format variables for printing.
