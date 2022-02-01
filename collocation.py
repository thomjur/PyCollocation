import sys
from collections import Counter
from nltk.tokenize import TweetTokenizer, word_tokenize
import re

def main(sentence, word, l, r):
    '''
        main function to start collocation analysis
    '''

    # start collocation analyses
    left_counter, right_counter, length, word_counter = collocation(sentence, word, l, r)

def collocation(document, word, l, r, tokenizer="standard"):

    # counter dict of words left of search term
    left_counter = Counter()
    # counter dict of words right of search term
    right_counter = Counter()
    # full counter - needed for later calculation (log-likelihood etc.)
    full_counter = Counter()

    # setting word to lower case and including regex
    word = re.compile(word.lower())
    # setting document to lower case
    document = document.lower()

    # select tokenizer (word is default; otherwise "tweet")
    if tokenizer == "standard":
        word_list = word_tokenize(document)
        ## only keeping words TODO: this might lead to wrong results as it currently is, better using stop word list later on
        word_list = [word for word in word_list if re.compile(r"\w+").match(word)]
    elif tokenizer == "tweet":
        tweet_tokenizer = TweetTokenizer()
        word_list = tweet_tokenizer.tokenize(document)

    # words in document
    length = len(word_list)
    # get word count of full document
    full_counter = Counter(word_list)

    # how often does the search term appear in document?
    word_counter = word_list.count(word)

    # main function to collect words left/right of search term
    for i in range(len(word_list)):
        # check if word matches the current token in the document taking into account regex
        match = word.match(word_list[i])
        if match:
            for x in range(1,int(l)+1):
                if i-x >= 0:
                    left_counter.update([word_list[i-x]])

            for x in range(1,int(r)+1):
                if i+x < length:
                    right_counter.update([word_list[i+x]])

    return full_counter, left_counter, right_counter

if __name__ == "__main__":
    '''
        argvs: document (str), Searchterm (str), L-Window (int), R-Window (int)
    '''
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
