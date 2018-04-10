import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

def zad3():
    #first particle in the middle of our 'canvas'
    rect_side = 10
    aggregationParticleList = []
    for i in range(-rect_side/2, rect_side/2):
        # print i
        aggregationParticleList.append([i, -rect_side/2])
        aggregationParticleList.append([i, rect_side/2])
        aggregationParticleList.append([-rect_side/2, i])
        aggregationParticleList.append([+rect_side/2, i])

    # print aggregationParticleList

    while not [0, 0] in aggregationParticleList:
        # print 'inside main loop'
        randomParticle = [rect_side + 4, rect_side + 4]#for moment any const value so  we can pass first comparison
        # print checkIfConnectedToOthers(randomParticle, aggregationParticleList)
        first = True
            
        # newPosition = [0, 0]
        while(first or not checkIfConnectedToOthers(randomParticle, aggregationParticleList)):
            
            if first == True:
                randomParticle = [0, 0]
                first = False
                # print 'im here'
            # print 'im here2'
            
            randomValue =    random.randint(0,100)
            # print randomValue
            if randomValue >= 0 and randomValue < 25:#first option is: we go up and right        
                newPosition = [randomParticle[0] + 1, randomParticle[1] + 1]
            elif randomValue >= 25 and randomValue < 50:#second optoin is: we go up and left
                newPosition = [randomParticle[0] - 1, randomParticle[1] + 1]
            elif randomValue >= 50 and randomValue < 75:#third option is: we go left and down
                newPosition = [randomParticle[0] - 1, randomParticle[1] - 1]
            else: #fourth option is we go right down
                newPosition = [randomParticle[0] + 1, randomParticle[1] - 1] 
            # print newPosition
            #update position with randomized step
            randomParticle = newPosition
            # print randomParticle
            
        if checkIfConnectedToOthers(randomParticle, aggregationParticleList):
            aggregationParticleList.append(randomParticle)
        # print len(aggregationParticleList)
    
    #spliting data into two independent arrays with seperated x, y values
    x_values = []   
    y_values = []
    
    for i in range(0, len(aggregationParticleList) - 1):
        x_values.append(aggregationParticleList[i][0])
        y_values.append(aggregationParticleList[i][1])
        

    # plt.title('Random aggregation fractal generator')
    #finally we are able to display our data
    plt.plot(x_values,y_values, 'o')
    plt.show()

def checkIfNotOut(particle):#returns True, when param particle is outside our circle's field, else returns False
    # print 'distance', math.sqrt((particle[0]**2 + particle[1]**2 ))
    radius = 150
    # print 'radius size', radius
    if math.sqrt((particle[0]**2 + particle[1]**2 )) > radius:
        # print 'is out'
        return True
    else:

        # print particle, 'still inside circle'
        return False

def checkIfConnectedToOthers(newParticle, aggregationParticleList):#checks if potentiall new particle is should be connected in current position, True for yes- should, False for no- shouldn't
    if [newParticle[0] + 1, newParticle[1] + 1] in aggregationParticleList or [newParticle[0] - 1, newParticle[1] + 1] in aggregationParticleList or [newParticle[0] - 1, newParticle[1] - 1] in aggregationParticleList or [newParticle[0] + 1, newParticle[1] - 1] in aggregationParticleList:
    # if [0, 0] in aggregationParticleList:
        return True       
    return False#shouldn't be connected


print zad3()