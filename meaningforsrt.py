
import nltk
def meani(word): #returns meaning of the input word 
    
    
   
    from nltk.corpus import wordnet

    
    
    syns=wordnet.synsets(word,pos=(wordnet.VERB))
    temp=list()
    
    for syn in wordnet.synsets(word):
        
        temp.append(syn.definition())
    
            
        
  
    if len(temp)>0:
        return temp[0]
    else:
        return " not valid "
