
import nltk
def mean(nontrivial): # returns a nested list with word in first index and meanings in the other indices
    nontrivial=list(set(nontrivial))
    
   
    from nltk.corpus import wordnet

    main=list()
    for i in range(len(nontrivial)): 
        syns=wordnet.synsets(nontrivial[i],pos=(wordnet.VERB))
        temp=list()
        temp.append(nontrivial[i])
        for syn in wordnet.synsets(nontrivial[i]):
            
            temp.append(syn.definition())
        main.append(temp)  
            
        
  
    return main
