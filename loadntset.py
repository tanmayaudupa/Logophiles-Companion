import numpy as np
from sklearn import preprocessing
import tkfile as x

def predict(t,w):
    
    seed=1 
 
    dataset = np.loadtxt(t, delimiter=",") #loading testing data 
    X=dataset[:,0:3]
    print(X.shape)
    y=dataset[:,3:]
    #Sigmoid Function
    def sigmoid (x):
        return(1/(1 + np.exp(-x)))

    #Derivative of Sigmoid Function
    def derivatives_sigmoid(x):
        return(x * (1 - x))

    X=preprocessing.normalize(X) #normalizing the data 

    #Variable initialization
    epoch=100#Setting training iterations
    lr=0.01 #Setting learning rate  
    inputlayer_neurons = 3 #number of features in data set
    hiddenlayer_neurons = 2 #number of hidden layers neurons
    output_neurons = 1 #number of neurons at output layer
    batch_size=1
    #weight and bias initialization from saved txt files
    temp1=np.loadtxt("bh.txt",dtype="float",delimiter=",")
    wh=np.loadtxt("wh.txt",dtype="float",delimiter=",")
    temp2=np.loadtxt("wout.txt",dtype="float",delimiter=",")
    temp3=np.loadtxt("bout.txt",dtype="float",delimiter=",")
    bh=np.array([temp1.tolist()])
    wout=np.array([[i] for i in temp2.tolist()])
    bout=np.array([temp3.tolist()])


##    feed forward on testing data

    hidden_layer_input1=np.dot(X,wh)
    hidden_layer_input=hidden_layer_input1 + bh
    hiddenlayer_activations = sigmoid(hidden_layer_input)
    output_layer_input1=np.dot(hiddenlayer_activations,wout)
    output_layer_input= output_layer_input1+ bout
    output = sigmoid(output_layer_input)
    E = y-output
    

    l=output.tolist() # l has predicted output values
    l2=list() # l2 has rounded values (0,1)
    for i in l:
        if i[0]>0.55 :
            l2.append(1)
##            print("1")
            
        else:
            l2.append(0)
##            print("0")

    wordslist=[]        
    a=open(w,"r")
    for i in a: # wordlist is list of the words in the video
        wordslist.append(i)
    temp5=list(zip(wordslist,l2)) #temp5 is nested list with first index as word and second as predicted value(0,1)
    nontrivial=[] #list of all the nontrivial words 
    for i in temp5:
        if i[1]==1:
            nontrivial.append(i[0][:len(i[0])-1])

    return(nontrivial)
