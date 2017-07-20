import collections
import string
import re, string
def importtxt(e): #creates a file with words in a differnt lines 
    f=open("organisedsubtitles.txt","w")
    t=open(e,"r")
    s=t.read()
    out = re.sub('[%s]' % re.escape(string.punctuation), '', s)
    l=out.split()
    for i in l:
            if i.isalpha():
               f.write(i.lower()+"\n")
    f.close()
    t.close()



    
