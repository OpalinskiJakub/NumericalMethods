import numpy as np
import matplotlib.pyplot as plt


n = 100
#x=np.random.rand(100)
#x=np.zeros(100)
x=[]
for i in range (1,101):
    x.append(i)

print(x)
b=list(range(1, n + 1))
err = []
iteration=[]
err2 = []
iteration2=[]


def jacobiMethod(x1,errornorm):
    iterator=0

    while True:
        x2 = x1.copy()
        x1[0] = (b[0]-x2[1]-0.2*x2[2])/3
        x1[1] = (b[1] - x2[0] - x2[2]-0.2*x2[3])/3
        for i in range(2,n-2):
                x1[i] = (b[i] - 0.2*x2[i-2]- x2[i-1]-x2[i+1]- 0.2*x2[i+2])/3
        x1[n-2] = (b[n-2] -0.2*x2[n-4] - x2[n-1]- x2[n-3])/3
        x1[n-1] = (b[n-1]  - 0.2*x2[n-3]- x2[n-2])/3
        norm=rightSolution()
        norm1=np.absolute(x1-norm)
        norm1=np.linalg.norm(norm1)
        err.append(norm1)
        print(norm1)
        iterator=iterator+1

        iteration.append(iterator)
        
        if norm1<errornorm :
            break
        
    print("Metoda Jacobiego")
    print(x1)    


def rightSolution():
    A=np.zeros((100,100))
    np.fill_diagonal(A, 3)
    A=A+(np.diag(np.ones(n-1), 1))
    A=A+np.diag(np.ones(n-1), -1)
    A=A+0.2*np.diag(np.ones(n-2), -2)
    A=A+0.2*np.diag(np.ones(n-2), 2)

    B=np.arange(1, 101)

    x=np.linalg.solve(A, B)
    
    return x

def gaussSeidelMethod(x1,errornorm):
    iterator=0
    
    x1=x1.copy()
    while True:
        y = x1.copy()
        x1[0] = (b[0]-x1[1]-0.2*x1[2])/3
        x1[1] = (b[1] - x1[0] - x1[2]-0.2*x1[3])/3
        for i in range(2,n-2):
                x1[i] = (b[i] - x1[i-1] - 0.2*x1[i-2]-x1[i+1]-0.2*x1[i+2])/3
        
        x1[n-2] = (b[n-2] -0.2*x1[n-4]- x1[n-3] - x1[n-1])/3
        x1[n-1] = (b[n-1]  - 0.2*x1[n-3]- x1[n-2])/3
        norm=rightSolution()
        norm1=np.absolute(x1-norm)
        norm1=np.linalg.norm(norm1)
        err2.append(norm1)
        iterator=iterator+1
        print(norm1)
        iteration2.append(iterator)
        
        if norm1<errornorm:
            break

        
        
        
    
    for i in range(1,40):
        iterator=iterator+1
        iteration2.append(iterator)
        err2.append(norm1)
    
    print("Metoda Gauusa")
    print(x1)

def printsolution():
        jacobiMethod(x.copy(),10**(-13))
        gaussSeidelMethod(x.copy(),10**(-13))   
        plt.grid(True)
        plt.ylabel("Bład")
        plt.xlabel("Iteracja")
        plt.yscale("log")
        plt.plot(iteration,err)
        plt.plot(iteration2, err2)
        plt.legend(['Jacobi', 'Gauss-Seidel'])
       # plt.savefig("prob0.eps")
        plt.show()
           





printsolution()
