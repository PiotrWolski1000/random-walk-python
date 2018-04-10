import random
# import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# import math

def zad1():
    aggregationParticleList = [[0, 0]]

    while not checkIfNotOut(aggregationParticleList):#repeat while there is not particle outside canvas
        #add new particle to aggregationParticleList to random position  
        randomParticle = random.randint(0, len(aggregationParticleList) -1)#first chose particle already in List
        #print aggregationParticleList[randomParticle]

        #generate new random position X and Y which is random between old_pos + [- 1, 1]
        randomValue = random.randint(0,100)

        if randomValue < 25:#first option is: we go up and right        
            newPosition = [aggregationParticleList[randomParticle][0] + 1, aggregationParticleList[randomParticle][1] + 1]

        elif randomValue < 50:#second optoin is: we go up and left
            newPosition = [aggregationParticleList[randomParticle][0] - 1, aggregationParticleList[randomParticle][1] + 1]
        elif randomValue < 75:#third option is: we go left and down
            newPosition = [aggregationParticleList[randomParticle][0] - 1, aggregationParticleList[randomParticle][1] - 1]
        else: #fourth option is we go right down
            newPosition = [aggregationParticleList[randomParticle][0] + 1, aggregationParticleList[randomParticle][1] - 1] 

        if newPosition not in(aggregationParticleList):
            aggregationParticleList.append(newPosition)
        
    #printing positions of all particles
    # for i in range(0, len(aggregationParticleList)-1):
    #     print aggregationParticleList[i]

            

        
    return 0

def checkIfNotOut(particleList):#return true if one of particles is outside my 'canvas'- max, else False
    max = 10
    for i in range(0, len(particleList)):
        if particleList[i][0] > max or particleList[i][0] < -max:
            return True 
        elif particleList[i][1] > max or particleList[i][1] < -max:         
            return True
    return False

print zad1()