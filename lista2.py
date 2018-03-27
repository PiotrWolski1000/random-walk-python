import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

def dt_pos(): 
    lista  = []
    while (len(lista) <= 99 ):
        tempX = random.randint(-1,1)
        if(tempX != 0):
            if len(lista) != 0:
                lista.append(tempX+lista[-1])
            else:
                lista.append(tempX)


    x = np.linspace(0, 99, 100)

    plt.title('zad1 lista 2')
    plt.xlabel('dt')
    plt.ylabel('location')

    plt.plot(x, lista, '-o')

    plt.show()

def dt_pos_2_subplots():
    lista  = []
    lista2 = []
    while (len(lista) <= 99 ):
        tempX = random.randint(-1,1)
        tempX2 = random.randint(-1,1)
        if(tempX != 0 and tempX2 != 0):
            if len(lista) != 0:
                lista.append(tempX+lista[-1])
            else:
                lista.append(tempX)

            if len(lista2) != 0:
                lista2.append(tempX2+lista2[-1])
            else:
                lista2.append(tempX2)


    x1 = x2 = np.linspace(1, 100, 100)

    plt.subplot(2, 1, 1)
    plt.plot(x1, lista, 'o-')
    plt.title('2 paths')
    plt.ylabel('position')

    plt.subplot(2, 1, 2)
    plt.plot(x2, lista2, 'o-')
    plt.xlabel('N')
    plt.ylabel('position')

    plt.show()

def histogram(N = 100000):
    lista  = []
    lastStepsList = []

    for i in range(1, N):
        lista = []
        while (len(lista) <= 99 ):
            tempX = random.randint(-1,1)
            if(tempX != 0):
                if len(lista) != 0:
                    lista.append(tempX+lista[-1])
                else:
                    lista.append(tempX)
        lastStepsList.append(lista[-1])
    
    plt.hist(lastStepsList)
    plt.show()

  
def zad1():
    print dt_pos()
    print dt_pos_2_subplots()
    print histogram()


zad1()