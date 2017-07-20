from itertools import chain
from nltk.corpus import wordnet



def noofsyn(text): # returns no of synonyms of the word
  synonyms = wordnet.synsets(text)
  lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
  return len(lemmas)

