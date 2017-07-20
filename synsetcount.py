import nltk
from nltk.corpus import wordnet as wn
def synsetcount(var): #returns no of synsets of the word
    
  p=wn.synsets(var)
  return len(p)

