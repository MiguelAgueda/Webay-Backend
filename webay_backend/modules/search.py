import json
from operator import itemgetter

def score_similarity(target_terms, listed_terms):
    target_set = set(target_terms)
    listed_set = set(listed_terms)
    return len(target_set.intersection(listed_set))


def search_titles(user_terms, list_of_listings):
    scored_list = []
    target_terms = user_terms.lower().split(' ')
    
    for listing in list_of_listings:  # Loop over list of listings.
        sku = listing[0]
        title_terms = listing[1].lower().split(' ')  # Index 1 is Title.
        score = score_similarity(target_terms, title_terms)
        listing.append(score)
        scored_list.append(listing)

    return sorted(scored_list, key=itemgetter(-1), reverse=True)  # Sort last element (score).


def load_data(path_to_file):
    """ Return data from specified JSON file."""
    with open(path_to_file, 'r') as file:
        data = json.load(file)
        file.close()
        return(data)


if __name__ == "__main__":

    list_of_listings = load_data("data_files/sample_listings.json")
    ordered_matches = search_titles(search_terms, list_of_listings)
