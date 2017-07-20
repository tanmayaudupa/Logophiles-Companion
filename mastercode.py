import scrab as sc
import synsetcount as syns
import synonymcount as syno
import syllablecount as syll
import freqcount as freq
global f

def inputfile(x): # returns a file with attributes/values  
   f=open(x,"r")
   z="values.txt"
   d=open(z,"w")
   count=0
   for word in f:
     temp=word.strip()
     count+=1
     l=len(word)
     d.write(str(syll.nsyl(temp))+","+str(freq.freq(word))+","+str(sc.scrab(temp))+",0"+"\n")
   f.close()
   d.close()
   return(z)







