import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random


def zad1(N = 10000):
    allWalkerPaths = []
    walkLength = 1000
    for i in range(0, N):
        walkerPath = []
        pos = [0, 0, 0]#pos[x,y]] initialization at every new walker
        randomValue = 0
        while(len(walkerPath) != walkLength):
            randomValue = random.uniform(0.0,99.996)

            if randomValue >= 0 and randomValue < 16.666:#first option is: we go up and right
                pos = [pos[0] + 1, pos[1], pos[2]]
            elif randomValue >= 16.666 and randomValue < 33.332:
                pos = [pos[0], pos[1] + 1, pos[2]]    
            elif randomValue >= 33.332 and randomValue < 49.998:#second optoin is: we go up and left
                pos = [pos[0], pos[1], pos[2] + 1]    
            elif randomValue >=49.998 and randomValue < 66.664:#third option is: we go left and down
                pos = [pos[0] - 1, pos[1], pos[2]]    
            elif randomValue >=66.664 and randomValue < 83.333:#fourth option is: we go down and right 
                pos = [pos[0], pos[1] - 1, pos[2]]    
            elif randomValue >=83.333 and randomValue <= 99.996:
                pos = [pos[0], pos[1], pos[2] - 1]
            walkerPath.append(pos)#updating WalkerPath
        allWalkerPaths.append(walkerPath)#updating list containing all paths of each walker (N-element list)

    #our data structure -> allWalkerPaths = [Walker = [ pos = [pos[0] pos[1]]], Walker, Walker]

    #here, outside of for loop we are finally able to show our result on the screen with some graphic chart
    #but first we have to split our date to two different arrays so: 

    x_values = []
    y_values = []
    z_values = []
    #to prevent memory usage for this task we display first element of array, because I want to call this function with N = 1 (look task info)
    for i in range(0,walkLength):
        x_values.append(allWalkerPaths[0][i][0])
        y_values.append(allWalkerPaths[0][i][1])
        z_values.append(allWalkerPaths[0][i][2])



    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.title('Random Walk 3D- walk')
    #finally displaying our data
    ax.plot(x_values, y_values, z_values, label='parametric curve')
    plt.show()

zad1(1)