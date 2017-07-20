q=open("trivial_value.txt","r")
w=open("non_trivial_value.txt","r")
o=open("allvalues.txt","w")
import random as ran
count=0
cnt=0
u=0
p=0

while u!=4023: #shuffles the entire file (eachline)
    r=ran.randint(1,4)
    count+=1
    if count%2==0 or p==1:
        
       
          
        
        for i in range(r):
            e=q.readline()
            o.write(e.strip()+"\n")
            cnt+=1
            
    if count%2!=0 and p!=1 :
     
        for i in range(r):
            e=w.readline()
            
                
            o.write(e.strip()+"\n")
            cnt+=1
            if e=="EOF":
                p=1
                
                
    u+=1
print(cnt)
q.close()
w.close()
o.close()
