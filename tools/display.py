import pandas as pd

'''
collection of functions to properly display output from analyses
'''

def output_top_collocates(left_counter, right_counter, k=3):
    '''
    function to print top collocates with pandas
    '''
    # collecting top k left words
    df_left = pd.DataFrame.from_dict(left_counter, orient="index", columns=["freq"])
    df_left["orient"] = "left"
    # only top k rows
    df_left_sorted = df_left.sort_values("freq", ascending=False).iloc[:3,:]

    # collecting top k right words
    df_right = pd.DataFrame.from_dict(right_counter, orient="index", columns=["freq"])
    df_right["orient"] = "right"
    # only top k rows
    df_right_sorted = df_right.sort_values("freq", ascending=False).iloc[:3,:]

    # concat both DataFrames
    df_full = pd.concat([df_right_sorted, df_left_sorted])
    
    ### output
    print(df_full.sort_values("freq", ascending=False))