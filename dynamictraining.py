import trainnsave as sen
import mastercode as mc
def calltrain(x): # appends new values to allvalues.txt and retrains 
    newz=mc.inputfile(x)
    f=open(newz,"r")
    g=open("allvalues.txt","a")

    for i in f:
        g.write(i)
           
        
    
    sen.train("allvalues.txt")
    f.close()
    g.close()
