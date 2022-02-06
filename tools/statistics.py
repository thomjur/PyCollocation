import math
'''
TODO implement as class
several implementations of different statistics for collocation analyis;
mainly based on the implementations in Brezina et al. (2018). Statistics in Corpus Linguistics, 66ff.
'''

def MU(node_freq, collocate_freq, collocation_freq, total_tokens, l_window, r_window):
    '''
    calculate relation between observed frequency and baseline expected frequency (collocation_freq/E_11)
    '''
    return collocation_freq / expected_freq_baseline_E11_(node_freq, collocate_freq, total_tokens, l_window, r_window)

def z_score(node_freq, coll_freq, total_tokens, l_window, r_window):
    '''
    TODO: implement
    calculate relation between observed frequency and baseline expected frequengy (coll_freq - E_11) / sqrt(E11)
    '''
    exp_baseline_freq = expected_freq_baseline_E11_(node_freq, coll_freq, total_tokens, l_window, r_window)
    return (coll_freq - exp_baseline_freq) / math.sqrt(exp_baseline_freq)


def log_likelihood():
    '''
    TODO: implement
    implementation of the famous log-likelihood algorithm
    '''
    pass


## HELPER FUNCTIONS

def expected_freq_baseline_E11_(node_freq, coll_freq, total_tokens, l_window, r_window):
    '''
    calculate expected freq. of co-occurrence using a "shake-the-box" model (Brezina 2018, 69)
    '''
    return (node_freq * coll_freq * (l_window + r_window)) / total_tokens
