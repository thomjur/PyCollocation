from collocation import collocation
from collections import Counter
from tools import display
import re


def start_collocation_analysis(collection, search_term, l_window, r_window, statistic="freq"):
    '''
    main function to start collocation analysis
    arguments are:
        - COLLECTION: an iterable collection or generator that returns single documents/sentences as strings (preferably short ones < XXX words)
        - SERCH TERM: the search term for the collocation analysis
        - L = left window range
        - R = right window range
    '''

    # counter dict of words left of search term
    left_counter = Counter()
    # counter dict of words right of search term
    right_counter = Counter()
    # counter dict of all words
    full_counter = Counter()

    # collect collocations
    for doc in collection:
        fc, lc, rc = collocation(doc, search_term, l_window, r_window)
        left_counter += lc
        right_counter += rc
        full_counter += fc

    # how often does the search term appear in the text? 
    search_term_counter = 0
    pattern = re.compile(search_term.lower())
    for elem in full_counter.keys():
        if re.match(pattern, elem):
            search_term_counter += full_counter[elem]

    # display results
    display.get_results_collocates(left_counter, right_counter, full_counter, search_term_counter, l_window, r_window, statistic)

    return full_counter, left_counter, right_counter
