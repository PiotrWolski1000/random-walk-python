import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import math

def zad3(a = 5, N = 10000): 
    list_t_for_N = []

    for i in range(1, N+1):
        pos_x = a
        list_nth_path = []#for getting len of our path, till we go off the 'screen', later we add len param to list_t_for_N array, which we later display in diagram
        while(pos_x > 0 and pos_x < 2*a):#always place our 'wedrowniczek' on the the middle of our size screen 
            randomValue = random.randint(-1, 1)
            if (randomValue != 0):
                pos_x = pos_x + randomValue
                # print pos_x
                list_nth_path.append(pos_x)
        list_t_for_N.append(len(list_nth_path))#here we are already done with things i spoke in above comments

    #average value of T
    averageValueOfT = sum(list_t_for_N)/len(list_t_for_N)
    # print "Average value of T for a = ", a, " is equal to " , averageValueOfT, ". "
    return averageValueOfT

n = 10#how many differents a we want?

avarageT_ValueForDifferentAParameter = [] 

for i in range(5, n + 5 ):#we start from 5, that's why we add 5 in range function
    avarageT_ValueForDifferentAParameter.append(zad3(i,10000))
   


plt.title('zad3 lista 2')

plt.plot(avarageT_ValueForDifferentAParameter, '-o')
plt.show()




# print zad3()
