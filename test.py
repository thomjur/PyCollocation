from analysis import start_collocation_analysis
from collocation import collocation

'''
    some unit testing of collocation analysis
'''

def test_collocations(test_sentences):
    full_counter, left_counter, right_counter = collocation(test_sentences[0], "test", 3, 3)
    print(full_counter)
    assert right_counter["dolor"] == 0, "Should be 0"
    assert left_counter["dolor"] == 1, "Should be 1"

def test_start_collocation_analysis(test_sentences):
    full_counter, left_counter, right_counter = start_collocation_analysis(test_sentences, "test", 3, 3)
    assert left_counter["dolor"] == 2, "Should be 2"
    assert right_counter["dolor"] == 1, "Should be 1"

# test collection of tweets
test_sentences = ["Lorem ipsum dolor test sit amet, consectetuer adipiscing elit.", "Aenean commodo ligula dolor test eget dolor.", \
    "Aenean massa. Cum sociis natoque penatibus test et magnis dis parturient montes, nascetur ridiculus mus.", \
    "Donec quam felis, ultricies nec, pellentesque test eu, pretium quis, sem.", \
    "Nulla consequat massa quis enim. Donec pede test dolor justo, fringilla vel, aliquet nec, vulputate eget, arcu.", \
    "In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt."]

print(test_sentences[0])
test_collocations(test_sentences)
test_start_collocation_analysis(test_sentences)
