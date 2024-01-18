import numpy as np
import random
from nlpTrain import train
from nlpimport import Prediction
import copy

#percentage is the percentage to train from the dataset
data=np.load('data.npy')
data=data.tolist()
datacopy=copy.deepcopy(data)
l=[]
def test(percentage,data,n):
    l=[]
    for i in range(n):
        datacopy=copy.deepcopy(data)
        cardtrain=int(percentage*len(datacopy))
        data_to_train=[]
        for i in range(cardtrain):
            elem=random.choice(datacopy)
            data_to_train.append(elem)
            datacopy.remove(elem)
        train(data_to_train)
        count=0
        for i in datacopy :
            if Prediction(i[0])==i[1] :
                count+=1
            
        l.append(count/len(datacopy)*100)
    mean=np.mean(l)
    return mean

percentage=0.05
l=[]
i=100
while percentage<=1:
        l.append((percentage*100 , test(percentage,data,i)))
        percentage+=0.05
print(l)
