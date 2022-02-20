from analysis import start_collocation_analysis
from tools import display
import unittest

'''
    some unit testing of collocation analysis
'''

class GeneralUnitTest(unittest.TestCase):

    def setUp(self):
        '''
        init sentences for tests
        '''
        self.test_sentences = ["Lorem ipsum dolor test sit amet, consectetuer adipiscing elit.", "Aenean commodo ligula dolor test eget dolor.", \
            "Aenean massa. Cum sociis natoque penatibus test et magnis dis parturient montes, nascetur ridiculus mus.", \
            "Donec quam felis, ultricies nec, pellentesque test eu, pretium quis, sem.", \
            "Nulla consequat massa quis enim. Donec pede test dolor justo, fringilla vel, aliquet nec, vulputate eget, arcu.", \
            "In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt."]

    def test_collocations(self):
        '''
        Test for single sentence function
        '''
        full_counter, left_counter, right_counter = start_collocation_analysis(self.test_sentences[0], "Test", 3, 3, doc_type="single")
        self.assertEqual(right_counter["dolor"], 0)
        self.assertEqual(left_counter["dolor"], 1)
        self.assertEqual(full_counter["elit"], 1)

    def test_start_collocation_analysis(self):
        '''
        Test for array of sentences function fpr MULTIPLE documents
        '''
        full_counter, left_counter, right_counter = start_collocation_analysis(self.test_sentences, "Test", 3, 3)
        self.assertEqual(left_counter["dolor"], 2)
        self.assertEqual(right_counter["dolor"], 2)
        self.assertEqual(full_counter["nec"], 2)

    def test_regex(self):
        '''
        Test for regex in search term for SINGLE document
        '''
        full_counter, left_counter, right_counter = start_collocation_analysis(self.test_sentences[0], "Tes*", 3, 3, doc_type="single")
        self.assertEqual(right_counter["dolor"], 0)
        self.assertEqual(left_counter["dolor"], 1)

    # DOES NOT WORK YET    
    # def test_get_results_collocates(self):
    #     '''
    #     Test if get_results_collocates in display.py is executed without an error
    #     '''
    #     self.assertTrue(get_results_collocates(left_counter, right_counter, total_word_counter, search_term_counter, l_window, r_window, statistic, output_type, k=3))


    def test_tabular_output(self):
        '''
        test pretty print output
        this is currently no real test...
        '''
        full_counter, left_counter, right_counter = start_collocation_analysis(self.test_sentences, "Test", 3, 3)
        display.get_results_collocates(left_counter, right_counter, full_counter, 5, 3, 3, "mu", "print")
        self.assertTrue(True)

if __name__ == "__main__":
        unittest.main()
