import pandas as pd
from tools.statistics import *

'''
collection of functions to properly display output from analyses
'''

def get_results_collocates(left_counter, right_counter, total_word_counter, search_term_counter, l_window, r_window, statistic, k=3):
    '''Function to return top collocates.

    PARAMETERS
    ----
    TODO: docstring
    '''

    # merging l/r dicts to one dict
    total_counter = left_counter + right_counter

    # collecting top k words
    df_top_collocates = pd.DataFrame.from_dict(total_counter, orient="index")
    df_top_collocates = df_top_collocates.reset_index()
    df_top_collocates.columns = ["collocate", "coll_freq"]

    # check and add main orientation of each collocate
    df_top_collocates["orient"] = df_top_collocates.apply(lambda x: get_orientation_(left_counter, right_counter, x["collocate"]), axis=1)

    # add total appearance of collocate
    df_top_collocates["freq"] = df_top_collocates.apply(lambda x: total_word_counter[x["collocate"]], axis=1)
    
    # calculate selected statistic (if different than "freq")
    if statistic == "mu":
        df_top_collocates["statistic"] = df_top_collocates.apply(lambda x: MU(search_term_counter, x["freq"], x["coll_freq"], sum(total_word_counter.values()), l_window, r_window), axis=1)

    ### output
    if statistic != "freq":
        print(df_top_collocates.sort_values("statistic", ascending=False).reset_index().drop("index", axis=1))
    else:
        print(df_top_collocates.sort_values("freq", ascending=False).reset_index().drop("index", axis=1))


### helper functions


def get_orientation_(left_counter, right_counter, collocate):
    '''Helper function to check if collocate appears l/r/- of search term.
    '''
    if left_counter[collocate] > right_counter[collocate]:
        return "left"
    elif left_counter[collocate] < right_counter[collocate]:
        return "right"
    else:
        return "-"