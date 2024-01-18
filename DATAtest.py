from dataset import data
from nlpimport import Prediction
from DATAtoTRAIN import train
import numpy as np
l = [i for i in data if not any(np.array_equal(i, t) for t in train)]

def test1(test):
    count=0
    for i in test :
        if Prediction(i[0])==i[1] :
            count+=1
    if __name__=="__main__":
        print("Accuracy :",count/len(test)*100,"%")
    return count / len(test) * 100

test1(l)