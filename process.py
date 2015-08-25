import nltk, re
from nltk import word_tokenize

filename = "butterscotch-pudding.txt"
with open(filename) as f:
	raw = f.read()

units = ["teaspoon", "tsp", "tablespoon", "tbsp",  "cup"]

tokens = word_tokenize(raw)

lancaster = nltk.LancasterStemmer()
print([lancaster.stem(t) for t in tokens])

