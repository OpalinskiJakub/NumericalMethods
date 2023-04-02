import matplotlib.pyplot as plt
import numpy as np
def algorithm(x,a,b):
    xfromfunction=a
    yfromfunctions=b
    z=[]

    counter=0
    for i in xfromfunction:
        counter=counter+1
    n=counter
    yresult=0

    for i in range(n):
        result=1
        for j in range(n):
            if (j!=i):
                
                a=x-xfromfunction[j]
                b=xfromfunction[i]-xfromfunction[j]
                if(b!=0):
                    result =result*(a/b)
                z.append(result)
        temp= result*yfromfunctions[i]       
        yresult=yresult+temp
    return yresult

     



def XforA(n):
    x = []
    for i in range (0,n+1):
        tmpX=-1 + 2*i/(n) 
        x.append(tmpX)
    return x

def XforB(n):
    x = []
    for i in range (0,n+1):
        tmpX=np.cos((2*i+1)/(2*(n+1))*np.pi)
        x.append(tmpX)
    return x


def YforA(x):
    y = []
    n=len(x)
    for i in range (0,n):
        tmpY=1/(1+25*x[i]*x[i])
        y.append(tmpY)
    return y
    
def YforAnotherFunction(x):
    y = []
    n=len(x)
    for i in range (0,n):
        tmpY=(1+5*x[i])/(1+25*x[i]*x[i])
        y.append(tmpY)
    return y

def libalg(x,xfromfunction, yfromfunctions):
    return np.interp(x, xfromfunction, yfromfunctions)

def functionToCheck():
    xfor5=XforA(5)
    algorithmdY5=[]
    algorithmdY5b=[]
    rangeofX = np.arange(-1.0, 1., 0.01)
    for x in rangeofX:
        algorithmdY5.append(algorithm(x,xfor5,YforA(xfor5)))
    for x in rangeofX:
        algorithmdY5.append(np.interp(x, xfor5,YforA(xfor5)))
    print(algorithmdY5)
    print(algorithmdY5b)



def solutionforA():

    XforFunction=XforA(100)
    plt.plot(XforFunction,YforA(XforFunction),label="Funkcja")
    rangeofX = np.arange(-1.0, 1., 0.01)
    xfor5=XforA(5)
    xfor10=XforA(10)
    xfor9=XforA(9)
    algorithmdY5=[]
    algorithmdY10=[]
    algorithmdY9=[]
    for x in rangeofX:
        algorithmdY5.append(algorithm(x,xfor5,YforA(xfor5)))
    for x in rangeofX:
        algorithmdY10.append(algorithm(x,xfor10,YforA(xfor10)))
    for x in rangeofX:
        algorithmdY9.append(algorithm(x,xfor9,YforA(xfor9)))
    plt.plot(rangeofX,algorithmdY5, label="Wielomian interpolacyjny dla n=5")
    plt.plot(rangeofX,algorithmdY10, label="Wielomian interpolacyjny dla n=10")
    plt.plot(rangeofX,algorithmdY9, label="Wielomian interpolacyjny dla n=9")
    #plt.plot(rangeofX,algorithmdY9, label="Wielomian interpolacyjny dla n=17")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

def solutionforB():

    XforFunction=XforB(100)
    plt.plot(XforFunction,YforA(XforFunction),label="Funkcja")
    rangeofX = np.arange(-1.0, 1., 0.01)
    xfor5=XforB(5)
    xfor10=XforB(10)
    xfor9=XforB(9)
    algorithmdY5=[]
    algorithmdY10=[]
    algorithmdY9=[]
    for x in rangeofX:
        algorithmdY5.append(algorithm(x,xfor5,YforA(xfor5)))
    for x in rangeofX:
        algorithmdY10.append(algorithm(x,xfor10,YforA(xfor10)))
    for x in rangeofX:
        algorithmdY9.append(algorithm(x,xfor9,YforA(xfor9)))
    plt.plot(rangeofX,algorithmdY5, label="Wielomian interpolacyjny dla n=7")
    plt.plot(rangeofX,algorithmdY10, label="Wielomian interpolacyjny dla n=10")
    plt.plot(rangeofX,algorithmdY9, label="Wielomian interpolacyjny dla n=9")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()




def solutionforAforAnotherFunction():

    XforFunction=XforA(100)
    plt.plot(XforFunction,YforAnotherFunction(XforFunction),label="Funkcja")
    rangeofX = np.arange(-1.0, 1., 0.01)
    xfor5=XforA(5)
    xfor10=XforA(10)
    xfor9=XforA(9)
    algorithmdY5=[]
    algorithmdY10=[]
    algorithmdY9=[]
    for x in rangeofX:
        algorithmdY5.append(algorithm(x,xfor5,YforAnotherFunction(xfor5)))
    for x in rangeofX:
        algorithmdY10.append(algorithm(x,xfor10,YforAnotherFunction(xfor10)))
    for x in rangeofX:
        algorithmdY9.append(algorithm(x,xfor9,YforAnotherFunction(xfor9)))
    plt.plot(rangeofX,algorithmdY5, label="Wielomian interpolacyjny dla n=7")
    plt.plot(rangeofX,algorithmdY10, label="Wielomian interpolacyjny dla n=10")
    plt.plot(rangeofX,algorithmdY9, label="Wielomian interpolacyjny dla n=9")
   # plt.plot(rangeofX,algorithmdY9, label="Wielomian interpolacyjny dla n=18")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

def solutionforBforAnotherFunction():

    XforFunction=XforB(100)
    plt.plot(XforFunction,YforAnotherFunction(XforFunction),label="Funkcja")
    rangeofX = np.arange(-1.0, 1., 0.01)
    xfor5=XforB(5)
    xfor10=XforB(10)
    xfor9=XforB(9)
    algorithmdY5=[]
    algorithmdY10=[]
    algorithmdY9=[]
    for x in rangeofX:
        algorithmdY5.append(algorithm(x,xfor5,YforAnotherFunction(xfor5)))
    for x in rangeofX:
        algorithmdY10.append(algorithm(x,xfor10,YforAnotherFunction(xfor10)))
    for x in rangeofX:
        algorithmdY9.append(algorithm(x,xfor9,YforAnotherFunction(xfor9)))
    plt.plot(rangeofX,algorithmdY5, label="Wielomian interpolacyjny dla n=7")
    plt.plot(rangeofX,algorithmdY10, label="Wielomian interpolacyjny dla n=10")
    plt.plot(rangeofX,algorithmdY9, label="Wielomian interpolacyjny dla n=9")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()




z="1"
while(z!="0"):
    print("Zadanie numeryczne nr 7 Opalinski Jakub ")
    print("PodpunktA-Wpisz 1")
    print("PodpunktA-Wpisz 2")
    print("Rozwaienie dla x z podpunktu a dla innej funkcji-Wpisz 3")
    print("Rozwaienie dla x z podpunktu b dla innej funkcji-Wpisz 4")
    print("Porownanie z biblioteka numeryczna-Wpisz 5")
    print("Aby zakonczyc --Wpisz 0")
    z=input()
   
    if z=="1": 
        solutionforA();
    elif(z=="2"):
        solutionforB();
    elif(z=="3"):
        solutionforAforAnotherFunction();
    elif(z=="4"):
        solutionforBforAnotherFunction();
    elif(z=="5"):
        functionToCheck();
