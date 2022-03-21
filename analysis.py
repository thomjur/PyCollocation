from collocation import collocation
from collections import Counter
from tools import display
from pathlib import Path
from tools.exceptions import NoResultsException
import sys
import re

def start_collocation_analysis(collection, search_term, l_window="3", r_window="3", statistic="freq", doc_type="iterable", output_type="print"):
    '''Main function to start collocation analysis.
    
    arguments are:
        - COLLECTION: an iterable collection or generator that returns single documents/sentences as strings (preferably short ones < XXX words)
        - SERCH TERM: the search term for the collocation analysis
        - L = left window range
        - R = right window range
        - Statistic = statistic to use (default "freq")
        - doc_type = "iterable" | "folder" | "single"
        - output_type = "print" | "csv"
    '''

    # counter dict of words left of search term
    left_counter = Counter()
    # counter dict of words right of search term
    right_counter = Counter()
    # counter dict of all words
    full_counter = Counter()

    # TODO: collect collocations depending on input data 
    if doc_type == "folder":
        # in this case, the collection is a folder path
        directory = collection
        docs = Path(directory).glob("*")
        for doc in docs:
            with open(doc, "r") as f:
                doc = f.read()
                print(doc)
                fc, lc, rc = collocation(doc, search_term, l_window, r_window)
                left_counter += lc
                right_counter += rc
                full_counter += fc
    elif doc_type == "single":
        fc, lc, rc = collocation(collection, search_term, l_window, r_window)
        left_counter += lc
        right_counter += rc
        full_counter += fc
    elif doc_type == "iterable":
        for doc in collection:
            fc, lc, rc = collocation(doc, search_term, l_window, r_window)
            left_counter += lc
            right_counter += rc
            full_counter += fc

    # how often does the search term appear in the text? 
    search_term_count = 0
    pattern = re.compile(search_term.lower())
    for elem in full_counter.keys():
        if re.match(pattern, elem):
            search_term_count += full_counter[elem]

    # display results

    if search_term_count == 0:
        # error handling
        raise NoResultsException("Sorry, search term was not found or no documents were provided!")
    else:
        display.get_results_collocates(left_counter, right_counter, full_counter, search_term_count, l_window, r_window, statistic, output_type)

    return full_counter, left_counter, right_counter

if __name__ == "__main__":
    '''
        argvs: collection (iterable), Searchterm (str), L-Window (int), R-Window (int)
    '''
    collection = sys.argv[1]
    search_term = sys.argv[2]
    l_window = sys.argv[3]
    r_window = sys.argv[4]
    statistic = sys.argv[5]
    doc_type = sys.argv[6]
    output_type = sys.argv[7]

    ## starting program
    start_collocation_analysis(collection, search_term, int(l_window), int(r_window), statistic, doc_type=doc_type, output_type = output_type)