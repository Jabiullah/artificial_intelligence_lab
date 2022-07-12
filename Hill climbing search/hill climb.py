import random
import math
def init():
  l = [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]
  print("Given array is ", l)  
  return l
def getCost(li):
  cost = 0
  for i in range(len(li) - 1):
    for j in range(i ,len(li)):
      if li[i] > li[j]:
        cost = cost + 1
  return cost
def goalTest(cost):
  if cost == 0 :
    return True
  else:
    return False
def move(e):
  #print(e)
  #print(math.exp(e))
  if random.random() <= math.exp(e): 
    return True
  else:
    return False
def generateStateSimu(state, cost):
  #c = cost
  tempState = state.copy();
  #print(tempState)
  for i in range(len(state)):
    tempState = state.copy();
    #print(tempState)
    for j in range(i+1,len(state)):
      temp = tempState[i];
      #print("temp",temp)
      tempState[i] = tempState[j]
      tempState[j] = temp
      tempCost = getCost(tempState);
      if tempCost < cost :
        # state = tempState.copy();
        # cost = tempCost
        return tempState, tempCost
      elif tempCost == cost:
        if (move(-1)):
          return tempState, tempCost
      else:
        h = cost - tempCost
        if move(h):
          return tempState, tempCost     
def hillclimb():
  A = init();
  cost = getCost(A)
  print("total cost ",cost)
  while not goalTest(cost) :
    A, cost = generateStateSimu(A, cost);
    # print("The array is ", A, cost)      
  print("sorted array -> ", A)
hillclimb();