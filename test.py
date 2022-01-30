from analysis import start_collocation_analysis

'''
    some unit testing of collocation analysis
'''

# test collection of tweets
test_sentences = ["Lorem ipsum dolor test sit amet, consectetuer adipiscing elit.", "Aenean commodo ligula dolor test eget dolor.", \
    "Aenean massa. Cum sociis natoque penatibus test et magnis dis parturient montes, nascetur ridiculus mus.", \
    "Donec quam felis, ultricies nec, pellentesque test eu, pretium quis, sem.", \
    "Nulla consequat massa quis enim. Donec pede test justo, fringilla vel, aliquet nec, vulputate eget, arcu.", \
    "In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt."]

# start analysis
start_collocation_analysis(test_sentences, "test", 3, 3)
