import json
import time
import sys
from operator import itemgetter


class Search:
    def __init__(self):
        pass

    def score_similarity(self, target_terms, listed_terms):
        """Assign score based on similarity between two lists."""
        target_set = set(target_terms)  # Create set from target list.
        listed_set = set(listed_terms)  # Create set from listing list.
        # Return score (# matches).
        return len(target_set.intersection(listed_set))

    def search_titles(self, user_terms, list_of_listings):
        """Returns a list of listings matching user search terms."""
        scored_list = []  # Create empty list to store matches.
        # Create list of words from search-string.
        target_terms = user_terms.lower().split(' ')

        for listing in list_of_listings:  # Loop over list of listings.
            # Index 1 is listing title. Split into word list.
            title_terms = listing[1].lower().split(' ')
            # Get similarity score for this listing.
            score = self.score_similarity(target_terms, title_terms)

            if score:  # If the listing has at least one match,
                listing.append(score)  # append score to end of listing,
                scored_list.append(listing)  # add listing to match-list.

        # Return list sorted by last element (score).
        return sorted(scored_list, key=itemgetter(-1), reverse=True)

    def load_data(self, path_to_file):
        """ Return data from specified JSON file."""
        try:
            with open(path_to_file, 'r') as file:  # Open file as read-only.
                data = json.load(file)  # Load data from file.
                file.close()  # Close file.
                return(data)  # Return data extracted from file.
        except:
            print("File not found. Check if the file at " + path_to_file + 
                  " exists, or if you are in the correct directory when accessing this program")
            sys.exit(1)


if __name__ == "__main__":  # If this program is being called, run some tests.
    print("Testing search functions...")
    searcher = Search()  # Create a Search object.
    start_time = time.time()  # Save start time of program.
    search_terms = "New Black Belt"  # Assign test search.
    # Create set from search-string.
    target_set = set(search_terms.lower().split(' '))
    # Extract listings.
    list_of_listings = searcher.load_data("data_files/sample_listings.json")
    # Assert list data structure of listings.
    assert type(list_of_listings) is list
    assert type(list_of_listings[0]) is list

    # Search listings.
    ordered_matches = searcher.search_titles(search_terms, list_of_listings)
    # Number of listing-terms that must match search-terms.
    min_match_thresh = 2
    match_count = 0
    for listing in ordered_matches:  # Loop over matches.
        # Create set from each listing title.
        listed_set = set(listing[1].lower().split(' '))
        if len(target_set.intersection(listed_set)) < min_match_thresh:
            # If not enough matches are found,
            break  # stop looping over listings.
        # If enough matches found,
        match_count += 1  # Increment match_count.

    print("\nTest Complete  --  Results"
          + F"\nTop {match_count} listings contain at least"
          + F" {min_match_thresh} search terms.")

    end_time = time.time()  # Save program finish time.
    print(F"Test Runtime: {round(end_time - start_time, 4)} seconds.")
