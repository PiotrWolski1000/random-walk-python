import matplotlib
import matplotlib.pyplot as plt
import random
import os
import math

def createForest(size, p):#size is size of map (x, y), p is probability of square to be a tree
    wood = []

    for i in range(0, size):
        for j in range(0, size):
            if random.random() < p:
                wood.append([i,j, 'tree', 'not on fire'])#appending to wood array with coordinates [x,y] and information about if is a tree or is on fire 
            else: 
                wood.append([i, j, 'not tree', 'not on fire'])
    # print len(wood)
    return wood

# def displayForest(forestMap, t):#edit to show different types of trees and a fire
#     x = []
#     y = []
#     isTree = []
#     for i in range(0, len(forestMap) - 1):
#         x.append(forestMap[i][0])
#         y.append(forestMap[i][1])
#         isTree.append(forestMap[i][2])

#     plt.plot(x, y, 'o')
#     plt.savefig('foo1.png') 
    # plt.show()

def delImages():
    mydir =  os.getcwd()
    filelist = [ f for f in os.listdir(mydir) if f.endswith(".png") ]
    for f in filelist:
        os.remove(os.path.join(mydir, f))

    

def burn(forestMap):
    dt = 1#time step
    t = 0#time, 0 at start
    
    treesOnFire = startFire(getFirstColumn(forestMap))#return list of trees which are on fire,

    #now we should update forestMap with data from our startFire function
    for i in range(0, int(math.sqrt(len(forestMap)))):
        for j in range(0, len(treesOnFire)):
            
            if forestMap[i][0] == treesOnFire[j][0] and forestMap[i][1] == treesOnFire[j][1]:
                forestMap[i][3] = treesOnFire[j][3]#we were modyfin just this parameter
    

    #burn until isThereAFire is false(until there is no tree with 'on fire flag')
    
    while(isThereAFire):
        t = t + dt
        print len(spreadingFire(forestMap))
        print "t: ",t
        return 0
    #     print t
        # displayForest(forestMap, t)
        #loop every tree, and check if is on fire

def getFirstColumn(forestMap):#return firstColumn of trees
    firstColumn = []
    # while(not firstColumnTrees):#repreat until finds first and any 'tree' in any 'first', non-empty column
    for i in range(0, int(math.sqrt(len(forestMap)))):
        firstColumn.append(forestMap[i])
    # print firstColumn
    return firstColumn

def startFire(firstCollumn):#we set up fire on first column trees
    firstCollumnTrees = []
    for i in range(0, len(firstCollumn)):
        if(firstCollumn[i][2] == 'tree'):
            # print firstCollumn[i][2] 
            firstCollumn[i][3] = 'on fire'
            firstCollumnTrees.append(firstCollumn[i])
    # print firstCollumnTrees 
    print "first column trees which are on fire in the first step", firstCollumnTrees
    return firstCollumnTrees

def spreadingFire(forestMap):
    #this function is spreading a fire on all trees in their neighbour
    
    print "spreading fire" 

    for i in range(0, len(forestMap)):
        if(forestMap[i][2] == 'tree'):
            neighbours = getNeighbours(i, forestMap)#neighbour tree of each tree
            print "type of neighbours(getNeighbours function) object in spreading fire function, before changing on fire param", type(neighbours)
            print neighbours
            # print "length of list: ", len(neighbours)
            # if(len(neighbours) > 0):#if there are any neighbours 
            if(neighbours):#if there are any neighbours 
                for j in range(0, len(neighbours)):
                    #neighbours data should already be filtred
                    #if neighbours[j][2] == 'tree' and neighbours[j][3] == 'not on fire':
                    neighbours[j][3] = 'on fire'
                    print neighbours[j][3], 'is on fire!'
# ->
    print 'spreadingFire on these trees: ' ,neighbours
    return neighbours
#!!!!!
#IMPORTANT!!!

def from2DTo1DPos(row, col, side):
    return row*side + col

def from1DTo2DPos(iterator , side):#return pos [i, j], where i = [0<=i, j<=side], row, col
    # iterator  = iterator -1
    return [iterator / side, iterator % side ]
 

def getNeighbours(iterator, forestMap):#check if is it ok here with indexing when simulation star working!!!!
    
    neighbours = []
    size = len(forestMap)
    side = int(math.sqrt(size))
    
    print "searchin nearby trees of tree: ", forestMap[iterator]


    pretenderPos = [from1DTo2DPos(iterator, side)[0], from1DTo2DPos(iterator, side)[1]]#[row, col] - row- [0], col- [1]
    
    print 'pretenderPos: ', pretenderPos[0], pretenderPos[1]
    for i in range(0, side):
        for j in range(0, side):
            print "search indexes: [i,j]", [i,j],"is equal to value: ",forestMap[from2DTo1DPos(i ,j,side)]
            # print "field "
            #top right
            # if(forestMap[from2DTo1DPos(i - 1,j+1,side)][2] != 0 ):
                # print forestMap[from2DTo1DPos(i - 1,j+1,side)][2]
            print from2DTo1DPos(pretenderPos[0], pretenderPos[1], side)
            # return 0
            if (forestMap[from2DTo1DPos(pretenderPos[0]-1, pretenderPos[1]+1, side)][2] == 'tree'):
                neighbours.append(forestMap[from2DTo1DPos(pretenderPos[0]-1, pretenderPos[1]+1, side)])
    
            # for i in range(0, side):
            #     for j in range(0, side):
            #         if(i > 0)  and (j < side - 1) and (forestMap[from2DTo1DPos(pretenderPos[0]-1, pretenderPos[1]+1, side)][2] == 'tree') and (forestMap[from2DTo1DPos(pretenderPos[0]-1, pretenderPos[1]+1, side)][3] == 'not on fire'):
            #             print forestMap[from2DTo1DPos(pretenderPos[0]-1, pretenderPos[1]+1, side)]

            # if(pretenderPos[1] < side - 1  and pretenderPos[0] != 0 and forestMap[from2DTo1DPos(i - 1,j+1,side)][2] == 'is tree' and forestMap[from2DTo1DPos(i - 1,j + 1,side)][2] == 'is not on fire' and forestMap[from2DTo1DPos(i - 1,j + 1,side)] not in neighbours):
            #     neighbours.append(forestMap[from2DTo1DPos(i - 1,j + 1,side)])
            #     print forestMap[from2DTo1DPos(i - 1,j + 1,side)]
            #     print "top right"
            # #top
            # if(pretenderPos[0] > 0 and forestMap[from2DTo1DPos(i-1,j,side)][2] == 'is tree' and forestMap[from2DTo1DPos(i-1,j,side)][2] == 'is not on fire' and forestMap[from2DTo1DPos(i-1,j,side)] not in neighbours):
            #     neighbours.append(forestMap[from2DTo1DPos(i - 1,j,side)])
            #     print forestMap[from2DTo1DPos(i - 1,j,side)]
            #     print "top"
            # #top left
            # if(pretenderPos[1] > 0 and pretenderPos[0] > 0 and forestMap[from2DTo1DPos(i-1,j-1,side)][2] == 'is tree' and forestMap[from2DTo1DPos(i - 1,j - 1,side)][2] == 'is not on fire' and forestMap[from2DTo1DPos(i - 1, j - 1,side)] not in neighbours):
            #     neighbours.append(forestMap[from2DTo1DPos(i - 1,j - 1,side)])
            #     print forestMap[from2DTo1DPos(i - 1,j - 1,side)]
            #     print "top left"
            # #left
            # if(pretenderPos[1] > 0 and forestMap[from2DTo1DPos(i,j - 1,side)][2] == 'is tree' and forestMap[from2DTo1DPos(i, j - 1,side)][2] == 'is not on fire' and forestMap[from2DTo1DPos(i,j - 1,side)] not in neighbours):
            #     neighbours.append(forestMap[from2DTo1DPos(i,j - 1,side)])
            #     print forestMap[from2DTo1DPos(i,j - 1,side)]
            #     print "left"
            #bottom left
            # if(pretenderPos[1] > 0 and pretenderPos[0] > 0 and forestMap[from2DTo1DPos(i+1,j - 1,side)][2] == 'is tree' and forestMap[from2DTo1DPos(i + 1,j - 1, side)][2] == 'is not on fire' and forestMap[from2DTo1DPos(i + 1,j - 1,side)] not in neighbours):
            #     neighbours.append(forestMap[from2DTo1DPos(i + 1,j - 1,side)])
            # bottom
            # if(pretenderPos[0] < side - 1 and forestMap[from2DTo1DPos(i+1,j,side)][2] == 'is tree' and forestMap[from2DTo1DPos(i + 1,j, side)][2] == 'is not on fire' and forestMap[from2DTo1DPos(i + 1,j,side)] not in neighbours):
            #     neighbours.append(forestMap[from2DTo1DPos(i + 1, j,side)])
            #bottom right
            # if(pretenderPos[1] < side - 1 and pretenderPos[0] <  side - 1 and forestMap[from2DTo1DPos(i + 1, j + 1, side)][2] == 'is tree' and forestMap[from2DTo1DPos(i + 1, j + 1, side)][2] == 'is not on fire' and forestMap[from2DTo1DPos(i + 1,j + 1, side)] not in neighbours):
            #     neighbours.append(forestMap[from2DTo1DPos(i + 1, j + 1,side)])
            #right
            # if pretenderPos[1] < side - 1 and forestMap[from2DTo1DPos(i, j+1, side)][2] == 'is tree' and forestMap[from2DTo1DPos(i,j + 1, side)][2] == 'is not on fire' and forestMap[from2DTo1DPos(i,j + 1,side)] not in neighbours :
            #     neighbours.append(forestMap[from2DTo1DPos(i, j + 1,side)])
#->          

    # return 0
    print "neighbours of", pretenderPos," count: ", len(neighbours)
    return neighbours

def checkIfIsItOKToSetAFire(tree):
    if (tree[2] == 'tree' and tree[3] == 'not on fire'):
        return True
    else:
        return False

def isThereAFire(forestMap):#false if there is fire, otherwise true  
    for i in range(0, len(forestMap) - 1):
        if(forestMap[i][3] == 'on fire'):
            return True
    return False #no fire

def task1(): 
    print "script started"
    mForestMap = createForest(20, 0.6)

    delImages()#always delete images after last script run, be carefull 
    burn(mForestMap)
    



task1()