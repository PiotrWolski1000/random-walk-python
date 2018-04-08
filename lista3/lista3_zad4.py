import matplotlib
import matplotlib.pyplot as plt
import random


def zad4(N = 10, h = 100):
    height = h
    differentHeights = []
    for i in range(0, 10):#10, const, because we want values for several height values
        allWalkerPaths = []
        
        for i in range(1, N + 1): 
                
            pos = [0, height*i]
            walkerPath = []
            randomValue = 0
            firstTimeRide = True

            while(firstTimeRide or walkerPath and not walkerPath[len(walkerPath)-1][1] == 0):
                randomValue = random.randint(0,100)
                
                #save method
                if(firstTimeRide):
                    firstTimeRide = not firstTimeRide
                
                # print "ich bin hier!" 
                if randomValue >= 0 and randomValue < 60:#first option is: we go up 
                    pos = [pos[0], pos[1] + 1 ]
                elif randomValue >= 60 and randomValue < 70:#second(10%) we go down
                    pos = [pos[0], pos[1] - 1]    
                elif randomValue >= 70 and randomValue < 85:#second optoin is: we go left
                    pos = [pos[0] - 1, pos[1]]    
                elif randomValue >=85 and randomValue <= 100:#third option is: we go right
                    pos = [pos[0] + 1, pos[1]]    
                walkerPath.append(pos)#updating WalkerPath
            allWalkerPaths.append(walkerPath)#updating list containing all paths of each walker (N-element list)
            # print len(allWalkerPaths)
    differentHeights.append(allWalkerPaths)
    #our data structure differentHeight-> allWalkerPaths = [Walker = [ pos = [x, y]], Walker, Walker]

    #here, outside of for loop we are finally able to show our result on the screen with some graphic chart
    #but first we have to split our date to two different arrays so: 
    
    # print allWalkerPaths

    # print len(differentHeights)#should be 10
    # print len(allWalkerPaths)#should be N
    # print len(allWalkerPaths[len(allWalkerPaths)-1])
    # print walkerPath

    # averageFreeFallTime = []#for different hieght

    # temp = 0
    myWalkerSum = 0
    myAllWalkersSum = []
    # myDifferentHeightsAverageSum = []#average for different heights array
    



    for i in range(0, len(differentHeights) ):
        myWalkerSum = 0
        for j in range(0, len(differentHeights[i]) ):
            myWalkerSum = myWalkerSum + len(differentHeights[i][j])    #count average distance for each walker
        myAllWalkersSum.append(myWalkerSum/len(differentHeights[i][j]))#size should be same as different heights amount
    

    print "heights: ", len(differentHeights)
    # print differentHeights[5][0]
    print len(myAllWalkersSum)

    #     for l in range (0, len(myAllWalkersSum) - 1 ):
    #         temp = temp + len(myAllWalkersSum[l])
    #         # print myAllWalkersSum[l]          
    #     if(j  == len(differentHeights[i][j])-1):
    #         myDifferentHeightsAverageSum.append(myAllWalkersSum/len(differentHeights[i][j]))
    #     myAllWalkersSum = []#making array null again


    # for i in range(0, 10):#differentHeights
    #     for j in range(0, len(allWalkerPaths[i]) - 1):#allWalkerPaths
    #         print j
    #         for k in range(0, len(walkerPath[j]) - 1):#walkerPath
    #             myWalkerSum = myWalkerSum + len(walkerPath[k])    #count average distance for each walker
    #             # print 'ich bin hier!'    
    #             # print myWalkerSum
    #             # print k
    #             if (k == len(walkerPath[j]) - 1):
    #                 print 'ich bin nicht im hier!'
                    
    #                 myAllWalkersSum.append(myWalkerSum/len(walkerPath[k]))

    #     # print myAllWalkersSum
    #     for l in range (0, len(myAllWalkersSum) - 1 ):
    #         temp = temp + len(myAllWalkersSum[l])
    #         print myAllWalkersSum[l]          


    #     if(j  == len(allWalkerPaths[i])):
    #         myDifferentHeightsAverageSum.append(myAllWalkersSum/len(allWalkerPaths[i]))
    #         # myAllWalkersSum = []#making array null again
    # x_values = []   
    # y_values = []

    # print 'different heights: ', myDifferentHeightsAverageSum

    # plt.title('Random-Walk 2D Drop of the Rain')
    # #finally displaying our data
    # plt.plot(x_values,y_values, 'o-')
    # plt.show()

zad4(1)