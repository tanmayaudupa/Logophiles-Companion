import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
def train(x):
    #Input array
    #X=np.array([[1,0,1,0],[1,0,1,1],[0,1,0,1]])
    seed=1
    #Output
    #y=np.array([[1],[1],[0]])
    dataset = np.loadtxt("allvalues.txt", delimiter=",")
    X=dataset[:,0:3]
    print(X.shape)
    y=dataset[:,3:]
    X_train,X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=seed)
    #Sigmoid Function
    def sigmoid (x):
        return(1/(1 + np.exp(-x)))

    #Derivative of Sigmoid Function
    def derivatives_sigmoid(x):
        return(x * (1 - x))

    X_train=preprocessing.normalize(X_train)

    #Variable initialization
    epoch=100#Setting training iterations
    lr=0.01 #Setting learning rate  
    inputlayer_neurons = 3 #number of features in data set
    hiddenlayer_neurons = 2 #number of hidden layers neurons
    output_neurons = 1 #number of neurons at output layer
    batch_size=1
    #weight and bias initialization
    wh=np.random.uniform(low=-1,high=1,size=(inputlayer_neurons,hiddenlayer_neurons))
    bh=np.random.uniform(low=-1,high=1,size=(1,hiddenlayer_neurons))
    wout=np.random.uniform(low=-1,high=1,size=(hiddenlayer_neurons,output_neurons))
    bout=np.random.uniform(low=-1,high=1,size=(1,output_neurons))

    for i in range(epoch):

    ##    FORWARD PROPAGATION

        hidden_layer_input1=np.dot(X_train,wh)
        hidden_layer_input=hidden_layer_input1 + bh
        hiddenlayer_activations = sigmoid(hidden_layer_input)
        output_layer_input1=np.dot(hiddenlayer_activations,wout)
        output_layer_input= output_layer_input1+ bout
        output = sigmoid(output_layer_input)
        E = y_train-output


    ##    BACK PROPAGATION
        
        slope_output_layer = derivatives_sigmoid(output)
        #print(slope_output_layer.shape)
        slope_hidden_layer = derivatives_sigmoid(hiddenlayer_activations)
        #print(slope_hidden_layer.shape)
        d_output = E * slope_output_layer
        Error_at_hidden_layer = d_output.dot(wout.T)
        d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
        wout += hiddenlayer_activations.T.dot(d_output) *lr
        bout += np.sum(d_output, axis=0,keepdims=True) *lr
        wh += X_train.T.dot(d_hiddenlayer) *lr
        bh += np.sum(d_hiddenlayer, axis=0,keepdims=True) *lr


    print(output)
    l=output.tolist()
    l2=list()
    for i in l:
        if i[0]>0.55 :
            l2.append(1)
            #print(i[0],"1")
        else:
            l2.append(0)
            #print("0")

    l1=y_train.tolist()
    correct=0
    incorrect=0
    for i in range(len(l1)):
        if l1[i][0]==l2[i]:
            correct+=1
        else:
            incorrect+=1
    print(correct,incorrect)
    np.savetxt("bh.txt",bh,delimiter=",")
    np.savetxt("wh.txt",wh,delimiter=",")
    np.savetxt("bout.txt",bout,delimiter=",")
    np.savetxt("wout.txt",wout,delimiter=",")
