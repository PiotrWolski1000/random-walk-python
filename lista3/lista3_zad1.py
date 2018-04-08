import matplotlib
import matplotlib.pyplot as plt
import random

def zad1(N = 10000):
    allWalkerPaths = []

    for i in range(0, N + 1):
        walkerPath = []
        pos = [0, 0]#pos[x,y]] initialization at every new walker
        randomValue = 0
        while(len(walkerPath) != 100):
            randomValue = random.randint(0,100)

            if randomValue >= 0 and randomValue < 25:#first option is: we go up and right
                pos = [pos[0] + 1, pos[1] + 1]
                
            elif randomValue >= 25 and randomValue < 50:#second optoin is: we go up and left
                pos = [pos[0] - 1, pos[1] + 1]
            elif randomValue >=50 and randomValue < 75:#third option is: we go left and down
                pos = [pos[0] + 1, pos[1] - 1]
            else:#fourth option is: we go down and right 
                pos = [pos[0] + 1, pos[1] - 1 ]
            
            
            walkerPath.append(pos)#updating WalkerPath
        allWalkerPaths.append(walkerPath)#updating list containing all paths of each walker (N-element list)

    #our data structure -> allWalkerPaths = [Walker = [ pos = [pos[0] pos[1]]], Walker, Walker]

    #here, outside of for loop we are finally able to show our result on the screen with some graphic chart
    #but first we have to split our date to two different arrays so: 

    x_values = []
    y_values = []
    
    #check if any walker end up in start point, which is pos[0, 0]
    looped = 0#defines numbers of our walkers which ended up in start point
    for i in range(0, N+1):
        print allWalkerPaths[i][99]
        if allWalkerPaths[i][99] == [0, 0]:
            looped = looped +1

    print "This is how many walkers ended up in start point max(", N, "): ", looped

    #choosing specific object data, lets say 10nth child to display
    for i in range(0,100):
        x_values.append(allWalkerPaths[10][i][0])#10th element,
        y_values.append(allWalkerPaths[10][i][1])

    #finally displaying our data
    plt.title('Random Walk 2D- walk')
    plt.plot(x_values,y_values, 'o-')
    plt.show()

zad1(10000)