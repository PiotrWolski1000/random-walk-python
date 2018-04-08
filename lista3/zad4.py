import matplotlib
import matplotlib.pyplot as plt
import random


def zad4(N = 10, h = 100):
    height = h
    differentHeights = []

    averageFreeTimeForDifferentHeights = []

    for j in range(1, 11):#10, const, because we want values for several height values
        allWalkerPaths = []
        for i in range(1, N+1):       
            pos = [0, height*j]
            walkerPath = []
            randomValue = 0
            firstTimeRide = True

            # while(firstTimeRide or walkerPath and not walkerPath[len(walkerPath)-1][1] == 0):
            while(pos[1] != 0):
                randomValue = random.randint(0,100)

                

                if(firstTimeRide):
                    firstTimeRide = not firstTimeRide
                
                if randomValue >= 0 and randomValue < 60:#first option is: we go down
                    pos = [pos[0], pos[1] - 1 ]
                elif randomValue >= 60 and randomValue < 70:#second(10%) we go up
                    pos = [pos[0], pos[1] + 1]    
                elif randomValue >= 70 and randomValue < 85:#second optoin is: we go left
                    pos = [pos[0] - 1, pos[1]]    
                elif randomValue >=85 and randomValue <= 100:#third option is: we go right
                    pos = [pos[0] + 1, pos[1]]
                # print pos
                walkerPath.append(pos)#updating WalkerPath
            allWalkerPaths.append(walkerPath)
        differentHeights.append(allWalkerPaths)
        # averageFreeTimeForDifferentHeights.append(sum(len(allWalkerPaths[j]))/N)
    print "each height len", len(allWalkerPaths)
    print "heights array len: ",len(differentHeights)

    myWalkerSum = 0
    myAllWalkersSum = []#average free fall time for each height

    for i in range(0, len(differentHeights) ):
        myWalkerSum = 0
        for j in range(0, len(differentHeights[i])):
            myWalkerSum = myWalkerSum + len(differentHeights[i][j])    #count average distance for each walker
        myAllWalkersSum.append(myWalkerSum/len(differentHeights[i]))#size should be same as different heights amount
   
    print myAllWalkersSum


zad4(100)