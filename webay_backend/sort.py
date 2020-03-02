from listing_editor import ListingEditor

editor = ListingEditor()

class QuickSort:
    def __init__(self):
        pass
    
    def low_to_high(self, pathtofile):
        listings = editor.safe_read(pathtofile)
        data_size = len(listings)
        
        if(data_size <= 1):
            return listings

        else:
            piv_listing = listings.pop()
            piv = piv_listing[2]
            numbers_bigger = []
            numbers_smaller = []
            sorted_list = []

            for listing in listings:

                if listing[2] > piv:
                  numbers_bigger.append(listing)
                else:
                  numbers_smaller.append(listing)

            sorted_list = self.low_to_high(numbers_smaller) 
                            + [piv_listing]+ self.low_to_high(numbers_bigger)
        return sorted_list 
               

    def high_to_low(self, pathtofile):
        listings = editor.safe_read(pathtofile)
        data_size = len(listings)
        
        if(data_size <= 1):
            return listings

        else:
            piv_listing = listings.pop()
            piv = piv_listing[2]
            numbers_bigger = []
            numbers_smaller = []
            sorted_list = []

            for listing in listings:

                if listing[2] > piv:
                  numbers_bigger.append(listing)
                else:
                  numbers_smaller.append(listing)

            sorted_list = self.high_to_low(numbers_smaller) 
                        + [piv_listing]+ self.high_to_low(numbers_bigger)
        return sorted_list            
