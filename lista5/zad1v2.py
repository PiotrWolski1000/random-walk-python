import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
import os
import math
import sys

# wood 'map' legend
# 0- not a tree
# 1- tree
# 2- tree on fire
# 3- burned tree

def createForest(size, p):#size is size of map (x, y), p is probability of square to be a tree
    wood = np.zeros((size, size), dtype='int32')#making wood with no trees

    #start spowning trees
    for i in range(0, size):
        for j in range(0, size):
            if random.random() < p:
                # wood.append([i,j, 'tree', 'not on fire'])#appending to wood array with coordinates [x,y] and information about if is a tree or is on fire
                wood[i][j] = 1
            #else we're leaving field with earlier zero(no else statement cause we have earlier created array with zeros method)

    print wood
    return wood

def delImages():
    mydir =  os.getcwd()
    filelist = [ f for f in os.listdir(mydir) if f.endswith(".png") ]
    for f in filelist:
        os.remove(os.path.join(mydir, f))

def task1(size, p):#size is size of wood (a=b side), p is probability
    print ("script has started")
    mForestMap = createForest(size, p)
    delImages()#always delete images after last script run, be carefull
    burn(mForestMap, size)

def burn(forestMap, size):
    dt = 1#time step
    t = 0#time, 0 at start

    treesOnFire = startFire(forestMap, size)#return list of trees(THE WHOLE MAP OF FOREST) which are on fire,

    #now we should update forestMap with data from our startFire function
    for i in range(0, size):
        for j in range(0, size):
            forestMap[i][j] = treesOnFire[i][j]

    print 'forest after fire was setted up: \n' , forestMap

    #burn until isThereAFire is false(until there is no tree with 'on fire flag'(#2)) or

    while(isThereAFire):
        t = t + dt
        fireWasSpread = spreadingFire(forestMap, size)
        #update forestMap with results from upper function(spreadingFire)
        print len(fireWasSpread)
        
        if(len(fireWasSpread) == 0):
            print 'there is not more trees to spread fire on!'
            return 0
        else:
            for i in range(0, size):
                for j in range(0, size):
                    forestMap[i][j] = treesOnFire[i][j]

        displayForest(forestMap, size, t)

def startFire(mForestMap, size):#we set up fire on first column trees
    # firstCollumnOnFire = []
    for i in range(0, size):
        if(mForestMap[i][0]):
            mForestMap[i][0] = 2
            # firstCollumnOnFire.append(m)
    return mForestMap

def spreadingFire(mForestMap, size):
    for x in range(0, size):
        for y in range(0, size):
            neighbours = getNeighbours(mForestMap, size)
            print 'neighbours array len after first turn' , len(neighbours)
    #so here is the moment we have neighbours to spread fire on,
    #i think here is the best place to turn old trees into carbon, so we should check, which one are they, and turn their flags to 3(burned tree)

    #changing old trees on fire to burned trees(#3 flag)
    for i in range(0, size):
        for j in range(0, size):
            if(mForestMap[i][j] == 2):
                mForestMap[i][j] = 3

    # be sure that neighbours exist
    # if not neighbours:
    #     return -1

    #now, we have to set up neighbour trees of last burning trees on fire
    for item in neighbours:
        mForestMap[item[0]][item[1]] = 2

    #print neighbours
    #print mForestMap
    return mForestMap

def getNeighbours(mForestMap, size):
    neighbours = []
    for i in range(0, size):
        for j in range(0, size):#checks if neighbour square is a tree and if it is, adds square(tree) to neighbours array
            if(mForestMap[i][j] == 2 and [i, j] not in neighbours):
                #left upper corner, that's why i and j params have to be greater than 0
                if(i > 0 and j > 0 and mForestMap[i - 1][j - 1] == 1):
                    neighbours.append([i - 1, j - 1])
                #middle up
                elif(j > 0 and mForestMap[i][j - 1] == 1):
                    neighbours.append([i, j - 1])
                #right upper corner,
                elif(i < size and j > 0 and mForestMap[i + 1][j - 1] == 1):
                    neighbours.append([i + 1, j - 1])
                #simply left side from the 'center' square, i is smaller by 1, and j should be the same level
                elif(i > 0 and mForestMap[i - 1][j] == 1):
                    neighbours.append([i - 1, j])
                #left bottom corner, i smaller by 1, j greater by 1
                elif(i > 0 and j < size and mForestMap[i - 1][j + 1] == 1):
                    neighbours.append([i - 1, j + 1])
                #bottom middle
                elif(j < size and mForestMap[i][j + 1] == 1):
                    neighbours.append([i, j + 1])
                #bottom right corner, both i,j are greater by 1
                elif(i < size and j < size and mForestMap[i + 1][j + 1] == 1):
                    neighbours.append([i + 1, j + 1])
                #just right, i greater by 1, j same level
                elif(i < size and mForestMap[i + 1][j]):
                    neighbours.append([i + 1, j])
    return neighbours

# wood 'map' legend
# 0- not a tree
# 1- tree
# 2- tree on fire
# 3- burned tree

def displayForest(forestMap, side, t):#edit to show different types of trees and a fire
    x_tree = []
    y_tree = []

    x_treeOnFire = []
    y_treeOnFire = []

    x_burnedTree = []
    y_burnedTree = []

    x_notTree = []
    y_notTree = []

    for i in range(0, side):
        for j in range(0, side):
            if(forestMap[i][j] == 0):
                x_notTree.append(i)
                y_notTree.append(j)
            elif(forestMap[i][j] == 1):
                x_tree.append(i)
                y_tree.append(j)
            elif(forestMap[i][j] == 2):
                x_treeOnFire.append(i)
                y_treeOnFire.append(j)
            else:
                x_burnedTree.append(i)
                x_burnedTree.append(j)

    plt.title('image for t =' + str(t))
    plt.ylabel('y position')
    plt.ylabel('x position')
    plt.plot(x_tree, y_tree, 'g^')

    # plt.plot(x_tree, y_tree, 'g^', x_burnedTree, y_burnedTree, 'ks', x_notTree, y_notTree, 'ks', x_treeOnFire, y_treeOnFire, 'r^')
    # plt.plot(x_burnedTree, y_burnedTree, 'ks')
    # plt.plot(x_notTree, y_notTree, 'gs')
    # plt.plot(x_treeOnFire, y_treeOnFire, 'r^')
    plt.savefig('a' + str(t) + '.png')
    # plt.show()



def isThereAFire(mForestMap, size):
    for i in range(0, size):
        for j in range(0, size): 
            if (mForestMap[i][j] == 2):
                return True
    return False

task1(20, 0.6)