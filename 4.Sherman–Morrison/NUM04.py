from timeit import default_timer as timer
import numpy as np
from matplotlib import pyplot as plt
import scipy.linalg as la

numbersOfMatrix=[]
time=[]
numbersOfMatrixWithNumericalLib=[]
timeNumericalLib=[] 

def createA(n):
    A =[[],[]]
    for i in range(n+1):
        A[0].append(9)
        A[1].append(7)
    A = np.array(A)
    return A

def createZ(n):
    
    m=n-1
    A=createA(m)
    z = np.zeros(m)
    z = list(z)
    z.insert(len(z),5/9)

    for i in range(0, m):
        a = (5 - (A[1][m] * z[m-i])) / A[0][m]
        z[m-i-1] = a

    z = np.array(z)
    z.reshape(m + 1, 1)
 
    return z

def createX(n):
    m=n-1
    A = createA(m)
    x = np.zeros(m)
    x = list(x)
    x.insert(len(x),1/9)

    for i in range(0, m):
        a = (1 - (A[1][m] * x[m-i])) / A[0][m]
        x[m-i-1] = a

    x = np.array(x)
    x.reshape(m + 1, 1)
    return x




def createU(n):
    u = []
    for i in range(n):
        u.append(1)
    u = np.array(u)
    u=u.reshape(n,1)
    return u


def createV(n):
    v =[]
    for j in range(n):
        v.append(1)
    v = np.array(v)
    v=v.reshape(1,n)
    return v



def createAforLib(n):
    a = np.zeros((n, n), np.double)

    np.fill_diagonal(a, 9)
    a=a+7*(np.diag(np.ones(n-1), 1))
    return a




def createB(n):
    B = []
    for i in range(n):
        B.append(5)
    B = np.array(B)
    B=B.reshape(n,1)
    return B

def numericalLibSolution(n):
    A = createAforLib(n)
    u = createU(n)
    v = createV(n)
    b = createB(n)
    Ahat = A + np.outer(u, b)
    LU, piv = la.lu_factor(A)

    def solveANumerical(b):
        return la.lu_solve((LU, piv), b)

    xhat = (np.linalg.inv(A + np.dot(u,v)) @ b)

    xhat2 = solveANumerical(b) - (solveANumerical(u) @ np.dot(v, solveANumerical(b))/(1+np.dot(v, solveANumerical(u))))

    return xhat2

def morrisonSolution(n):

    u=createU(n)
    x=createX(n)
    v=createV(n)
    z=createZ(n)
    morrison = z - ((x * np.dot(v,z))/(1+(np.dot(v,x))))
    return morrison.reshape(n,1)

def solveMyalgorithm():
    for i in range(100,4000,100):
        time1 = timer()
        morrisonSolution(i)
        time2 = timer()
        time.append(time2-time1)
        numbersOfMatrix.append(i)
        print(i)
        

def comparsion():
    for i in range(100,4000,500):
        time1 = timer()
        morrisonSolution(i)
        time2 = timer()
        time.append(time2-time1)
        numbersOfMatrix.append(i)
        time1n = timer()
        numericalLibSolution(i)
        time2n = timer()
        timeNumericalLib.append(time2n-time1n)
        numbersOfMatrixWithNumericalLib.append(i)
        print("Liczenie")
        



def start():
    z=1
    while(z!="0"):
        print("Zadanie numeryczne nr 4 Jakub Opalinski")
        print("1-Wyswietlenie wyniku rownania dla n=50.")
        print("2-Sprawdzenie z biblioteka numeryczna")
        print("3-Wyswietlenie wykresu wielkosci macierzy od czasu.")
        print("4-Wyswietlenie wykresu porownujacego moj algorytm z algorytmem napisanym przy pomocy biblioteki numerycznej.")
        print("0-Zakoncz program")
        z=input()
        if z=="1":
            print(morrisonSolution(50))
        elif z=="2":
            print(morrisonSolution(50))
            print("Sprawdzenie z biblioteka numeryczna:")
            print(numericalLibSolution(50))
            print("Roznica pomiedzy rozwiazaniami")
            print(morrisonSolution(50)-numericalLibSolution(50))
        elif z=="3":
            solveMyalgorithm()
            plt.title("Czas Wykonania od rozmiaru macierzy")
            plt.xlabel("Rozmiar macierzy(N)")
            plt.ylabel("Czas wykonania dla danej macierzy(s)")
            plt.plot(numbersOfMatrix, time)
            plt.show()
            numbersOfMatrix.clear()
            time.clear()
            numbersOfMatrixWithNumericalLib.clear()
            timeNumericalLib.clear() 
        elif z=="4":
            comparsion()
            plt.title("Czas Wykonania od rozmiaru macierzy-Porownanie")
            plt.xlabel("Rozmiar macierzy(N)")
            plt.ylabel("Czas wykonania dla danej macierzy(s)")
            plt.plot(numbersOfMatrix, time, label='Rozwiaznie z moim algorytmem')
            plt.plot(numbersOfMatrixWithNumericalLib,timeNumericalLib, label="Rozwiaznie z biblioteka numeryczna")
            plt.legend()
            plt.grid()
            plt.show()
            numbersOfMatrix.clear()
            time.clear()
            numbersOfMatrixWithNumericalLib.clear()
            timeNumericalLib.clear() 

start()

        