from nltk.corpus import cmudict
d = cmudict.dict()
def nsyl(word): # reurns no of syllables in the word / 1
   try:
    y=[len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
    return y[0]
   except:
      return 1
