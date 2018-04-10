import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

def zad2():
    #first particle in the middle of our 'canvas'
    n = 1000#n is how many particles we want to store in aggregationParticleList  
    aggregationParticleList = [[0, 0], [0,1], [0,-1]]
    max = 150
    while len(aggregationParticleList) < n:#repeat while there is 1k elements in particle array  
        print 'ilosc zlepkow: ', len(aggregationParticleList)
        randomParticle = [random.randint(-max, max), random.randint(-max, max)]#first chose particle already in List
        # randomParticle = [0,0]
        if ( checkIfNotOut(randomParticle)) and (randomParticle not in aggregationParticleList):#we have to be sure that our particle is inside our canvas and is not already in aggregationList
            #started our walk
            while (not checkIfNotOut(randomParticle)) or checkIfConnectedToOthers(randomParticle, aggregationParticleList):
                #randomWalkStart
                randomValue = random.randint(0,100)

                if randomValue >= 0 and randomValue < 25:#first option is: we go up and right        
                    newPosition = [randomParticle[0] + 1, randomParticle[1] + 1]

                elif randomValue >= 25 and randomValue < 50:#second optoin is: we go up and left
                    newPosition = [randomParticle[0] - 1, randomParticle[1] + 1]
                elif randomValue >= 50 and randomValue < 75:#third option is: we go left and down
                    newPosition = [randomParticle[0] - 1, randomParticle[1] - 1]
                else: #fourth option is we go right down
                    newPosition = [randomParticle[0] + 1, randomParticle[1] - 1] 

                #update position with randomized step
                randomParticle = [randomParticle[0]+newPosition[0], randomParticle[1]+newPosition[1]]
                print "test", randomParticle
                print aggregationParticleList
        
        #finally add new particle to list, but still under one condition
        if checkIfConnectedToOthers(randomParticle, aggregationParticleList):
            print "checkIfNotOut invoked and passed! now adding new partile to list"
            aggregationParticleList.append(randomParticle)
            
    print aggregationParticleList
    print 'final length: ', len(aggregationParticleList)#n+1 because of first element

    #spliting data into two independent arrays with seperated x, y values
    x_values = []   
    y_values = []
    
    for i in range(0, len(aggregationParticleList) - 1):
        x_values.append(aggregationParticleList[i][0])
        y_values.append(aggregationParticleList[i][1])
        

    plt.title('Random aggregation fractal generator')
    #finally we are able to display our data
    plt.plot(x_values,y_values, 'o')
    plt.show()

def checkIfNotOut(particle):#returns True, when param particle is outside our circle's field, else returns False
    print 'distance', math.sqrt((particle[0]**2 + particle[1]**2 ))
    radius = 150
    print 'radius size', radius
    if math.sqrt((particle[0]**2 + particle[1]**2 )) > radius:
        print 'is out'
        return True
    else:

        print particle, 'still inside circle'
        return False

def checkIfConnectedToOthers(newParticle, aggregationParticleList):#checks if potentiall new particle is should be connected in current position, True for yes- should, False for no- shouldn't
    
    # for i in range(0, len(aggregationParticleList)-1):#checks for each particle, if pottential new particle is in neighbour of already exists element of aggregationParticleList
    
    if [newParticle[0] + 1, newParticle[1] + 1] in aggregationParticleList or [newParticle[0] - 1, newParticle[1] + 1] in aggregationParticleList or [newParticle[0] - 1, newParticle[1] - 1] in aggregationParticleList or [newParticle[0] + 1, newParticle[1] - 1] in aggregationParticleList:
        return True        
    return False#shouldn't be connected


print zad2()