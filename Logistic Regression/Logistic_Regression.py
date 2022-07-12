#from sklearn import datasets
import numpy as np
from numpy import random
import math
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as p

iris = datasets.load_iris()
X = iris.data[:, :2]
y = (iris.target != 0) * 1

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 4)

#print(X.shape)
#print(y.shape)
#print(y)

train_list = []

for i in range(len(x_train)):
  k = np.insert(x_train[i], 0, 1)
  #print("k:", k)
  train_list.append(k)
  #print(train_list[i])

LR = [0.1, 0.01, 0.001, 0.0001, 0.00001] #For different lr values



for lr in LR:
    theta = [np.random.rand(), np.random.rand(), np.random.rand()]
    #print("THETA: ", theta)
    train_loss = []
    
    for i in range(1000):
        TJ = 0
        k = 0
        
        for X in train_list:
            Z = np.dot(X, theta)
            h = 1 / (1 + math.exp(-Z))
            J = -y_train[k] * np.log(h) - (1 - y_train[k]) * np.log(1 - h)
            TJ += J
            dv = X * (h - y_train[k])
            theta = theta - dv * lr
            k += 1
        TJ = TJ / len(x_train)
        train_loss.append(TJ)
    p.plot(train_loss)
    p.xlabel("Iteration")
    p.ylabel("Train_loss")
    p.show()
  
    test_list = []  
    for i in range(len(x_test)):
        k = np.insert(x_test[i], 0, 1)
        #print("k:", k)
        test_list.append(k)
        #print(train_list[i]) 
        
    correct = 0
    k = 0
    
    for X in test_list:
        Z = np.dot(X, theta)
        h = 1 / (1 + math.exp(-Z))
        if(h >= 0.5):
            h = 1
        else:
            h = 0
        if h == y_test[k]:
            correct += 1
        k += 1
    val_acc = (correct / len(y_test)) * 100
    print("LR: ", lr,"       ", "Val_acc: ", val_acc)    