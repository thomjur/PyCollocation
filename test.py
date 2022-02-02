from analysis import start_collocation_analysis
from collocation import collocation
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
        full_counter, left_counter, right_counter = collocation(self.test_sentences[0], "Test", 3, 3)
        self.assertEqual(right_counter["dolor"], 0)
        self.assertEqual(left_counter["dolor"], 1)

    def test_start_collocation_analysis(self):
        '''
        Test for array of sentences function
        '''
        full_counter, left_counter, right_counter = start_collocation_analysis(self.test_sentences, "Test", 3, 3)
        self.assertEqual(left_counter["dolor"], 2)
        self.assertEqual(right_counter["dolor"], 2)

    def test_regex(self):
        '''
        Test for regex in search term
        '''
        full_counter, left_counter, right_counter = collocation(self.test_sentences[0], "Tes*", 3, 3)
        self.assertEqual(right_counter["dolor"], 0)
        self.assertEqual(left_counter["dolor"], 1)

    def test_tabular_output(self):
        '''
        test pretty print output
        this is currently no real test...
        '''
        full_counter, left_counter, right_counter = start_collocation_analysis(self.test_sentences, "Test", 3, 3)
        display.get_results_collocates(left_counter, right_counter, full_counter)
        self.assertTrue(True)

if __name__ == "__main__":
        unittest.main()