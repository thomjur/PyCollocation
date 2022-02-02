import pandas as pd

'''
collection of functions to properly display output from analyses
'''

def get_results_collocates(left_counter, right_counter, total_word_count, k=3):
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
    df_top_collocates["freq"] = df_top_collocates.apply(lambda x: total_word_count[x["collocate"]], axis=1)
    
    ### output
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