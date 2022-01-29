import sys
from collections import Counter

def main(sentence, word, l, r):
    '''
        main function to start collocation analysis
    '''

    # start collocation analyses
    left_counter, right_counter, length, word_counter = collocation(sentence, word, l, r)

    # print for debugging
    print(f"Length: {length}\n\n\"{word}\" Count: {word_counter}\n\nLeft Words: {left_counter.most_common()}\n\nRight words: {right_counter.most_common()}\n")

def collocation(document, word, l, r):

    # counter dict of words left of search term
    left_counter = Counter()
    # counter dict of words right of search term
    right_counter = Counter()
    # full counter - needed for later calculation (log-likelihood etc.)
    full_counter = Counter()

    # setting word/document to lower case
    word = word.lower()
    document = document.lower()

    # TODO: implement nltk tokenizer
    word_list = document.split(" ")
    # words in document
    length = len(word_list)
    # get word count of full document
    full_counter = Counter(word_list)

    # how often does the search term appear in document?
    word_counter = word_list.count(word)

    # main function to collect words left/right of search term
    for i in range(len(word_list)):
        if word_list[i] == word:
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
