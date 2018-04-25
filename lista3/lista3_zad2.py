import matplotlib
import matplotlib.pyplot as plt
import random

#checks if given value already exists is array -> return true
def checkIfInside(arr, val):
    if val in arr:
        return True
    return False

def zad2(N = 10000):
    allWalkerPaths = []

    for i in range(0, N):
        walkerPath = []
        pos = [0, 0]#pos[x,y]] initialization at every new walker
        randomValue = 0
        #variables which can help us to find out if we are stuck in dot(can't move anywhere)
        up_right = True
        up_left = True
        down_left  = True
        down_right = True
        #creater walkerPath Object
        endWhile = False
        firstElementExist = True#initializate this variable here to True, before we started to create walkerPath array-object, so I can check if walkerPath exist or if its first element supposed to be added
        while(not endWhile):
            randomValue = random.randint(0,100)
            if up_right and randomValue >= 0 and randomValue < 25:#first option is: we go up and right
                pos = [pos[0] + 1, pos[1] + 1]
                if walkerPath and checkIfInside(walkerPath, pos):
                    up_right = False
            elif up_left and randomValue >= 25 and randomValue < 50:#second optoin is: we go up and left
                pos = [pos[0] - 1, pos[1] + 1]
                if walkerPath and checkIfInside(walkerPath, pos):
                    up_left = False
            elif down_left and randomValue >=50 and randomValue < 75:#third option is: we go left and down
                pos = [pos[0] + 1, pos[1] - 1]
                if walkerPath and checkIfInside(walkerPath, pos):
                    down_left = False
            elif down_right :#fourth option is: we go down and right 
                pos = [pos[0] + 1, pos[1] - 1 ]
                if walkerPath and checkIfInside(walkerPath, pos):
                    up_right = False

            if not up_right or not up_left or not down_left or not down_right:#first we need to check if we have any options to do
                endWhile = True
            elif  walkerPath or firstElementExist and not (checkIfInside(walkerPath, pos)):
                walkerPath.append(pos)#updating WalkerPath
                # print walkerPath
                firstElementExist = False#it will work without this line, but added just to be precize


        allWalkerPaths.append(walkerPath)#updating list containing all paths of each walker (N-element list)

    # print allWalkerPaths

    #in these two arrays we want to keep our data which we want to display
    x_values = []
    y_values = []
    
    dataBaseVariable = max(allWalkerPaths)#longes walk variable data storage
    # print len(max(allWalkerPaths))#function returning length of the longest walk

    #choosing specific object data, lets say 10nth child to display
    for i in range(0,len(dataBaseVariable)):
        x_values.append(dataBaseVariable[i][0])#10th element,
        y_values.append(dataBaseVariable[i][1])
    

    #finally displaying our data
    plt.title('Random Walk 2D- walk')
    plt.plot(x_values,y_values, 'o-')
    plt.show()

zad2(10000)



