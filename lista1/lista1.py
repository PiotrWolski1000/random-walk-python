#dependencies   
import random
import math

#N amount of points
def zad1(N):
    #checks if points are inside or outside the sphere with radius value of 1 
    value = 0
    for i in range(0, N):
        if not math.sqrt(random.uniform(-1, 1)**2 + random.uniform(-1, 1)**2 + random.uniform(-1, 1)**2) > 1:
            value += 1
    return (float(value)/float(N)*8.0)

def sphereCube():
    return ((4.0/3.0)*math.pi)

def zad1_showAnswers():
    print "sphere_cube: ", sphereCube()

    print "100, ", zad1(100)
    print "10 000, ", zad1(10000)
    print "1 000 000", zad1(1000000)

def zad2(N = 100000, dimension = 15):
    # sphere_volume = float(float(math.pow(2, 15)) * float(math.factorial(8)) * float(math.pow(math.pi, 7))) / float(math.factorial(16)) 
    succed = 0

    for j in range(0, N):
        value = 0.0
        
        for i in range(0, dimension):
            value = float(value) + float((random.uniform(-1.0, 1.0))**2)

        if value < 1.0:
            succed = succed + 1
        
    print float(float(succed)/float(N))*float(pow(2, 15))
    # print sphere_volume
    

def zad2_showAnswers(side_length  = 2):

    volume_cube = math.pow(side_length, 15) 
    print zad2()/volume_cube
     


def zad4(N = 10000):#N ilosc podejsc do problemu
    
    ilosc_trafien = []

    for j in range(0, N):
        box = range(100)
        random.shuffle(box)
        succed = 0
    
        for i in range(0, len(box)):
            if box[i] == i:
                succed = succed + 1
        ilosc_trafien.append(succed)#dodajemy ilosc "sukcesow do listy, aby pozniej zbadac srednia"  

    return float(sum(ilosc_trafien)/float(N))
    # print ilosc_trafien

def f1(x):
    return math.exp(-(x*x/2))

def zad3(m):
    a = -2
    b = 2
    d = b-a 
    n = m
    calka = 0

    for i in range(n):
        x = random.uniform(a, b)
        calka = calka + d * f1(x)
    calka /= math.sqrt(2*math.pi)
    calka = calka / n 
    print calka

zad1_showAnswers()
#print zad2()
# print zad3(100)
# print zad3(10000)
# print zad3(1000000)

# zad4(100000)