from analysis import start_collocation_analysis

'''
    some unit testing of collocation analysis
'''

# test collection of tweets
test_sentences = ["„ah das passt schon mein jonathan-laurenzius test hat die masern durchgemacht und wir sind alle daran gewachsen“...medien like \
    ~es gibt immer zwei seiten laden wir impfgegner_innen zu diskussionen ein bei 0 bis 1 verdachtsfällen test coronavirus like \
    https://t.co/BDOioZ2iyp", "Guten Morgen! :) Lest doch mal den Teil unten. Die chinesische Der #Partei selbst schreibt inzwischen: \
    Auch ohne Symptome ist man eine potentieller Virenschleuder. Man rechnet damit, test dass es deutlich länger dauernd wird als SARS.  \
    https://t.co/WzvZs0LpuX", "Das Weiße Haus teilt den Fluggesellschaften mit, dass es möglicherweise alle Flüge zwischen China \
    und den USA wegen des test Coronavirus Ausbruch aussetzen wird. https://t.co/hRsyrtVHZt", "Ich glaube halb #China hat schon das \
    #Coronavirus - jetzt ist es raus.", "@not_ur_muse @gerhardschwar11 test Apropos krankmachender Klima Abzock Hype Gottseidank \
    habe ich schon mein test Coronavirus Gegenmittel &amp; kann entspannt diesen neuen Megadeal abwarten, wenn sie das entsprechende \
    Gegenmittel sauteuer auf test Deine Kosten anbieten werden 🇩🇪😎🇻🇪#FreeAssange @NachDenkSeiten  @telepolis_news \
    https://t.co/Ols0pgevo1", "@tagesschau @heungkongyan1 Apropos krankmachender Klima test Abzock Hype Gottseidank habe ich schon mein \
    #Coronavirus Gegenmittel &amp; kann entspannt diesen neuen Megadeal abwarten, wenn sie das entsprechende Gegenmittel sauteuer \
    auf Deine Kosten anbieten 🇩🇪😎🇻🇪#FreeAssange #kenfm @nuoviso @SpiegelAnti @SZ @dpa https://t.co/UvLVnagUlG"]

# start analysis
start_collocation_analysis(test_sentences, "test", 3, 3)
