import numpy as np
from scipy.spatial import distance
from numpy import genfromtxt
import random

Data = np.genfromtxt(r"iris.csv",delimiter=",")
c = Data.T[-6] # class
#print(c)
S0=Data.T[-4] #first row
#print(S0[1])
S1=Data.T[-3] #second row
#print(S1)
S2=Data.T[-2] #third row
#print(S2)
S3= Data.T[-1] #forth row
#print(S3)
dataset = []
for i in range(1,len(S1)):
  t1=S0[i]
  t2=S1[i]
  t3=S2[i]
  t4=S3[i]
  t5=c[i]
  k = ','.join([str(t1),str(t2),str(t3),str(t4),str(t5)])
  dataset.append(k)
  #if i<3:
  #  print(k)
#print(dataset)
#list_check = isinstance(dataset,list)
#print(list_check)
Train_set = []
Val_set = []
Test_set = []
#[float(i) for i in dataset]

random.shuffle(dataset)
#print(dataset)

for S in range(len(dataset)):
  R = np.random.rand()
  if R >= 0 and R <= 0.7:
    Train_set.append(dataset[S])
  elif R >= 0.7 and R <= 0.85:
    Val_set.append(dataset[S])
  else:
    Test_set.append(dataset[S])

#print("Train Set")
#print(Train_set)

K=15
L=[]
temp_float_val_set = []
temp_float_train_set = []

for V in range(len(Val_set)):
  for T in range(len(Train_set)):
    #Distance hobe ,  distance.euclidean(Val_set[V - 1],Train_set[T - 1])
    x = Val_set[V - 1]
    #print(type(x))
    y = x.split(",")
    for i in range (len(y)):
      z=float(y[i])
      temp_float_val_set.append(z)
    
    x1 = Train_set[T - 1]
    y1 = x1.split(",")
    for i in range (len(y1)):
      z1=float(y1[i])
      temp_float_train_set.append(z1)

    #print(temp_float_val_set)
    #print(temp_float_train_set)
    dis = distance.euclidean(temp_float_val_set,temp_float_train_set)
    #print(dis)
    temp_float_val_set.clear()
    temp_float_train_set.clear()

    L.append([dis,Train_set[T]])
  L.sort()
#print(L)

count = 0

for i in range(K):
  if Val_set[i][4] == L[i][1][4]: 
    count =count+ 1
print()
print("Count : ", count)
acc = (count / K)

print("Validation accuracy :", acc)
