import nltk
from nltk.corpus import gutenberg
from nltk import bigrams
from nltk import trigrams
from collections import Counter
from collections import defaultdict
import random
import codecs
import re
eapStories = codecs.open("EAPStories.txt", 'r', encoding='utf-8',errors='ignore')

nonPunct = re.compile('.*[A-Za-z0-9].*')
filtered = [w for w in eapStories if nonPunct.match(w)]
filteredSTR = " ".join(str(x) for x in filtered)
dataDictionary = Counter(filteredSTR.split())
print(dataDictionary)

text = []
for x in range(1000):
   rand = random.random()
   accumulator = .0
   
   for word, freq in dataDictionary.items():
      accumulator = accumulator + freq/1000000
      if accumulator >= rand:
            text.append(word)
            break

print(' '.join(text))#too, no best than about clearly in know of in made of the the side one the of and the are customer From spots having found majority, from was been I-as Touch-me-Not a double The having armed dropped rank but which mer_. well week-once
