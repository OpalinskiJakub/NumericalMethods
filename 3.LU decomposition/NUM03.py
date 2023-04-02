import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt

time=[]
iteration=[]
time2=[]
iteration2=[]


def solutionWithMyAlgorithm(N):
    start = timer()
    g=[]
    
    A=np.zeros([N,4])
    LU=np.zeros([N,4])
    A[0][2]=0.1
    A[0][3]=0.4
    for i in range(0,N):

        if(i>0):
            A[i][0]=0.2
        A[i][1]=1.2
        if((i>0)):
            A[i-1][2]=0.1/i
        if((i>1)):
            A[i-1][3]=0.4/(i*i)
    x=[]
    for i in range(0,N):
        temp=1.
        x.append(temp+i*temp)
    y=x

    LU=A
    g.append(1)
    for i in range(1, N):
        z=i-1
        LU[i][0] = A[i][0]/LU[z][1]
        LU[i][1] = A[i][1]-LU[i][0]*LU[z][2]
        LU[i][2] = A[i][2]-LU[i][0]*LU[z][3]
        LU[i][3] = A[i][3]

    y[0]=x[0]
    y[1]=x[1]-LU[1][0]*y[0]
    y[2]=x[2]-LU[2][0]*y[1]
    
    for i in range(3, N):
        y[i]=x[i]-LU[i][0]*y[i-1]

    y[N-1]=x[N-1]/LU[N-1][1]
    y[N-2] = (x[N-2]-LU[N-2][2]*g[0]*y[N-1]*1*g[0])/LU[N-2][1]
    y[N-3]=(x[N-3]-LU[N-3][3]*y[N-1]-LU[N-3][2]*y[N-2]*g[0])/LU[N-3][1]
    for i in range(4,N+1):
        z=N-i
        y[z]=(x[z]-LU[z][3]*g[0]*y[z+2]-LU[z][2]*y[(N-i)+1])/LU[z][1]
    for i in range(4,N+1):
        if(y[z]!=(x[z]*g[0]-LU[z][3]*y[z+2]-LU[z][2]*y[(N-i)+1])/LU[z][1]):
            g[0]=1
        
    
    
    end = timer()
    print(end-start)
    time.append(end-start)
    print(y)
    u=1
    print("Wyznacznik:")
    for i in range(N):     
        u=u*LU[i][1]
    print(u)


def solutionWithNumpy(N):
    start2 = timer()
    A=np.zeros((N,N))
    np.fill_diagonal(A, 1.2)
    A=A+0.2*np.diag(np.ones(N-1), -1)
    z=[]
    for i in range(1,N):
        z.append(0.1/i)
    A=A+np.diag(z, 1)
    z=[]
    for i in range(1,N-1):
        z.append(0.4/(i*i))
    A=A+np.diag(z, 2)
    x=[]
    for i in range(0,N):
        temp=1.
        x.append(temp+i*temp)
    result=np.linalg.solve(A, x)
    end2 = timer()
    time2.append(end2-start2)
    print("Wyznacznik")
    print(np.linalg.det(A))
    print(result)


z="1"
while(z!="0"):
    print("Zadanie numeryczne nr 3 Opalinski Jakub ")
    print("Wyniki z biblioteka-Wpisz 1")
    print("Wyniki z moim algorytmem-Wpisz 2")
    print("Wykres-Wpisz 3")
    print("Wykres (porownanie )-Wpisz 3")
    print("Aby zakonczyc --Wpisz 0")
    z=input()
   
    if z=="1": 
       solutionWithNumpy(100)
    elif(z=="2"):
        solutionWithMyAlgorithm(100)
    elif(z=="3"):
        
        for i in range(100,600):
            solutionWithMyAlgorithm(i)
            iteration.append(i)
        
        print(iteration)
        print(time)
        plt.grid(True)
        plt.ylabel("Czas")
        plt.xlabel("Iteracja(N)")
        plt.plot(iteration,time)
    elif(z=="4"):
            
        for i in range(100,600):
            solutionWithMyAlgorithm(i)
            iteration.append(i)
                
        for i in range(100,600):
            solutionWithNumpy(i)
            iteration2.append(i)
            
        print(iteration)
        print(time)
        plt.grid(True)
        plt.ylabel("Czas")
        plt.xlabel("Iteracja(N)")
        plt.plot(iteration,time)
        plt.plot(iteration2,time2)
        plt.legend(['Moj algorytm', 'Biblioteka numeryczna'])


       