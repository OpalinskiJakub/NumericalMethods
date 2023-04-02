
import numpy as np
from matplotlib import pyplot as plt

z=1
while(z!="0"):
    print("Zadanie numeryczne nr 1.a) Opalinski Jakub ")
    print("double--Wpisz 64")
    print("float --Wpisz 32")
    print("Aby zakonczyc --Wpisz 0")
    z=input()
   
    if z=="64": 
        arr = np.array([1],dtype=np.float64)
        h=np.float64(1)
        
        for i in range (1,500):
            arr=np.append(arr,h)
            h=h*np.float64(0.91)     

        
        y=np.array(np.absolute(((np.sin(0.2+arr)-np.sin(0.2))/(arr))-np.cos(0.2)), dtype=np.float64)

   
        plt.plot(arr,y)
        plt.ylabel('f(h) (error)')
        plt.xlabel('h')
        plt.yscale("log")
        plt.xscale("log")
        plt.show()
    elif(z=="32"):
        arr = np.array([1],dtype=np.float32)
        h=np.float32(1)
        
        for i in range (1,500):
            arr=np.append(arr,h)
            h=h*np.float32(0.91)     

    
        y=np.array(np.absolute(((np.sin(0.2+arr)-np.sin(0.2))/(arr))-np.cos(0.2)), dtype=np.float32)

      
        plt.plot(arr,y)
        plt.ylabel('f(h) (error)')
        plt.xlabel('h')
        plt.yscale("log")
        plt.xscale("log")
        plt.show()
 


