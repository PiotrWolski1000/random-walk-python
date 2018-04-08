import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import math

def zad2(N = 100):
    lista  = []
    lista2 = []
    myLists = []
    myLists2 = []
    sum1 = 0
    sum2 = 0
    tempX = 1
    lastTempX = -1

    tempX2 = 1
    lastTempX2 = -1

    srednie = []
    srednie2 = []


    for i in range(0, N):
        sum1 = 0
        sum2 = 0
        lista = []
        lista2 = []
        srednia = 0
        srednia2 = 0

        while (len(lista) <= 99 ):
            
            randomValue = random.randint(1, 100)

            if randomValue <= 80:
                tempX = lastTempX

            else:
                tempX = -lastTempX
                lastTempX = tempX

            if len(lista) != 0:
                lista.append(tempX+lista[-1])
            else:
                lista.append(tempX)

            srednia = srednia+randomValue
            if(len(lista) == 100):
                srednia = srednia/100
                srednie.append(srednia)


#20% szansy na kontynuowanie

        while (len(lista2) <= 99 ):

            randomValue = random.randint(1, 100)

            if randomValue >= 80:
                tempX2 = lastTempX2

            else:
                tempX2 = -lastTempX2
                lastTempX2 = tempX2



            if len(lista2) != 0:
                lista2.append(tempX2+lista2[-1])
            else:
                lista2.append(tempX2)
            
            srednia2 = srednia2 + randomValue
            
            if(len(lista2) == 100):
                srednia2 = srednia2/100
                srednie2.append(srednia2)

        myLists.append(lista)
        myLists2.append(lista2)

#end of for loop
    # srednia1 = sum(myLists) / (len(myLists))    
    # srednia2 = sum(myLists2) /(len(myLists2))    
    

    # for i in range(0,99):
    print myLists[0]
    print "myLists[] length: ",len(myLists)
    print "srednie[] length: ",len(srednie)

    print "myLists2[] length: ",len(myLists2)
    print "srednie2[] length: ",len(srednie2)


    odchylenia1 = []
    odchylenia2 = []

    for d in range(0, N):
        odchylenie1 = 0
        odchylenie2 = 0
        for i in range(0, len(myLists[0])):
            odchylenie1 = odchylenie1 + pow(myLists[d][i]-srednie[d],2)
            odchylenie2 = odchylenie2 + pow(myLists2[d][i]-srednie2[d],2)
            if(i == 99):
                odchylenia1.append(math.sqrt(odchylenie1/(N-1)))
                odchylenia2.append(math.sqrt(odchylenie2/(N-1)))
                
    print "moje odchylenia to: "
    print odchylenia1[0]
    # print odchylenia2
   
    x = np.linspace(0, 99, 100)

    # print len(myLists)

    plt.title('zad2 lista 2')
    plt.xlabel('dt')
    plt.ylabel('location')
    plt.plot(x, myLists[0], '-o')
    plt.show()
    plt.plot(x, myLists[1], '-x')
    plt.show()
    plt.plot(odchylenia1, 'o')
    plt.show()
    plt.plot(odchylenia2, 'o')
    plt.show()


zad2(1000)

#srednia jest inna dla kazdego kroku n


# sum(x_i - _x)^2


