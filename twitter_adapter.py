import json
import os
import jsonlines
import gzip
from collocation import collocation
from collections import Counter
from glob import glob
from tools import display
import sys
import re

def twitter_collocates(directory, search_term, l_window="5", r_window="5", statistic="freq", api="1", output_type="print"):
    '''Main function to start collocation analysis with jsonl files cointaining tweets hydrated with twarc.

    arguments are:
        - DIRECTORY: a directory that contains jsonl files containing json objects which inlcude tweets (key "full_text")
        - SERCH TERM: the search term for the collocation analysis
        - L = left window range
        - R = right window range
        - Statistic = statistic to use (default "freq")
        - API: possibility to choose between files based on the twitter API 1/twarc and the API 2/twarc2
        - output_type = "print" | "csv"
    '''

    # counter dict of words left of search term
    left_counter = Counter()
    # counter dict of words right of search term
    right_counter = Counter()
    # counter dict of all words
    full_counter = Counter()

    #os.chdir(directory)
    # define variables
    tweetsnumber = 0
    search_term_count = 0

    if api == "1":
        for entry in glob(f"{directory}/*.jsonl.gz", recursive = True):
            with gzip.open(entry, "rb") as jsonlentry:
                reader = jsonlines.Reader(jsonlentry)
                for obj in reader:
                    if "full_text" in obj:  # checks if new tweet in json object
                        tweetsnumber += 1
                        fc, lc, rc = collocation(obj["full_text"], search_term, l_window, r_window)
                        left_counter += lc
                        right_counter += rc
                        full_counter += fc
                        if tweetsnumber % 10000 == 0:
                            print(f"Progress {tweetsnumber} tweets analysed.")

        # how often does the search term appear in the text?
        pattern = re.compile(search_term.lower())
        for elem in full_counter.keys():
            if re.match(pattern, elem):
                search_term_count += full_counter[elem]

    # Twitter API2 with different structure needs yet to be implemented
    if api == "2":
        print("----------- ERROR: This has not been implemented yet. Sorry! -----------")

    print("final results")
    # display results
    display.get_results_collocates(left_counter, right_counter, full_counter, search_term_count, l_window, r_window, statistic, output_type)



if __name__ == "__main__":
    '''
        argvs: Directory, Searchterm (str), L-Window (int), R-Window (int)
    '''
    directory = sys.argv[1]
    search_term = sys.argv[2]
    l_window = sys.argv[3]
    r_window = sys.argv[4]
    statistic = sys.argv[5]
    api = sys.argv[6]
    output_type = sys.argv[7]

    ## starting program
    twitter_collocates(directory, search_term, int(l_window), int(r_window), statistic, api="1", output_type = output_type)
