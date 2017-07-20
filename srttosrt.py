import os
import meaningforsrt as mf

def srttosrt(var,nt): #modifies srt file adding the meanings
    base=os.path.splitext(var)[0] #convert srt to txt file
    os.rename(var,base+"temp0.txt")
    f=open(base+"temp0.txt","r") # converted txt file from srt
    w=open(base+"formatedt.txt","w") # removing punc from txt file 
    o=f.read(1)
    while o!="":
        if o in ["?",".","!"]:
            w.write(" ")
        else:
            w.write(o)
        o=f.read(1)
    f.close()
    w.close()
    f=open(base+"formatedt.txt","r")
    w=open(base+"temp.txt","w")#new txt file with meanings 
    while True:
        r=f.readline()
        if r=="":
             w.write(r)
             break
        
        else:
            time=f.readline()
            
            w.write(time)
            r=f.readline()
            
            temp=[]
            while r!="\n":
                w.write(r)
                temp.extend(r.split())
                r=f.readline()
            
            for i in temp:
                
                if i.lower() in nt:
                    
                    w.write('<font color="#3399FF">'+i+" : "+mf.meani(i)+"</font>"+"\n")
                    
            w.write("\n")
    f.close()
    w.close()
    file=base+"temp.txt"
    os.rename(file,base+"EDITED.srt") #modified srt file 
    os.remove(base+"formatedt.txt")
    os.remove(base+"temp0.txt")
    os.remove(base+".txt")
    

    
