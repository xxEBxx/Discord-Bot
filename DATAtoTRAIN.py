from dataset import data
import random

data=data.tolist()
n=int(0.85*len(data))
train=[]
for i in range(n):
    elem=random.choice(data)
    train.append(elem)
    data.remove(elem)
if __name__=="__main__":
    print(len(train))



