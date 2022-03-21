'''
File containing custom exceptions for PyCollocation.
'''

class NoResultsException(Exception):
    '''
    Simple exception if no results were returned. Either because not existing folder was passed or search term not found. 
    '''
    pass