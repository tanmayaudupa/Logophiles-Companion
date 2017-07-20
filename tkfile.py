
import srttotxt as stt
import mastercode as mc
import loadntset as ls
from tkinter import *
import meanings as mn
global trivlist
import srttosrt as ss
import dynamictraining as dt
trivlist=list() #nested list with words and its meanings
 
def callme(fl):
     win=Tk()
     win.geometry('800x500+0+0')
     f=Frame(win)
     win.title("logophile's companion")

     lb = Listbox(win,height=500)
     lb.pack(fill=BOTH)
     
     sb = Scrollbar(win,orient=VERTICAL)
     sb.pack(fill=BOTH)
     sb.configure(command=lb.yview)
     lb.pack(fill=BOTH)
     lb.configure(yscrollcommand=sb.set)
     lb.curselection()
     if fl[len(fl.strip())-4:]==".srt": #checks if the file is srt or txt
          s=stt.importsrt(fl) 
     
     else:
          s=fl
    
     new=mc.inputfile(s) #extracts attributes of words into a new file 
     nontrivial=ls.predict(new,s) #classifies non trivial words 
     
     trivlist=mn.mean(nontrivial) 
     if fl[len(fl.strip())-4:]==".srt": 
          ss.srttosrt(fl,nontrivial) #replaces original srt with modified srt with meanings
     
     for i in trivlist: #addition of non trivial words with meanings into tkinter list box
        if len(i)>1:
             
             lb.insert(END,i[0].upper())
             lb.insert(END,"Definition :")
             
             for j in i[1:]:
                  lb.insert(END,j)
     r=open("newnontrivialwords.txt","w") 
     for word in nontrivial: 
         r.write(word+"\n")
     r.close()
     dt.calltrain("newnontrivialwords.txt") #retraining the network on new words from videos


