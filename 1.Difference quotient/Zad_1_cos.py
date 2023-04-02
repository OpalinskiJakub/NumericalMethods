
import numpy as np
from matplotlib import pyplot as plt

z=1
while(z!="0"):
    print("Zadanie numeryczne nr 1 dla cos Opalinski Jakub ")
    print("double dla a)--Wpisz cos.64.a")
    print("float dla a)--Wpisz cos.32.a")
    print("double dla b)--Wpisz cos.64.b")
    print("float dla b)--Wpisz cos.32.b")
    
    z=input()
   
    if (z=="cos.64.a"): 
        arr = np.array([1],dtype=np.float64)
        h=np.float64(1)
        
        for i in range (1,500):
            arr=np.append(arr,h)
            h=h*np.float64(0.91)     

        
        y=np.array(np.absolute(((np.cos(0.2+arr)-np.cos(0.2))/(arr))-((-1)*np.sin(0.2))), dtype=np.float64)

   
        plt.plot(arr,y)
        plt.ylabel('f(h) (error)')
        plt.xlabel('h')
        plt.yscale("log")
        plt.xscale("log")
        plt.show()
    elif(z=="cos.32.a"):
        arr = np.array([1],dtype=np.float32)
        h=np.float32(1)
        
        for i in range (1,500):
            arr=np.append(arr,h)
            h=h*np.float32(0.91)     

    
        y=np.array(np.absolute(((np.cos(0.2+arr)-np.cos(0.2))/(arr))-((-1)*np.sin(0.2))), dtype=np.float32)

      
        plt.plot(arr,y)
        plt.ylabel('f(h) (error)')
        plt.xlabel('h')
        plt.yscale("log")
        plt.xscale("log")
        plt.show()
    elif(z=="cos.64.b"): 
        arr = np.array([1],dtype=np.float64)
        h=np.float64(1)
        
        for i in range (1,500):
            arr=np.append(arr,h)
            h=h*np.float64(0.91)     

        
        y=np.array(np.absolute(((np.cos(0.2+arr)-np.cos(0.2-arr))/(2*arr))-((-1)*np.sin(0.2))), dtype=np.float64)

   
        plt.plot(arr,y)
        plt.ylabel('f(h) (error)')
        plt.xlabel('h')
        plt.yscale("log")
        plt.xscale("log")
        plt.show()
    elif(z=="cos.32.b"):
        arr = np.array([1],dtype=np.float32)
        h=np.float32(1)
        
        for i in range (1,500):
            arr=np.append(arr,h)
            h=h*np.float32(0.91)     

    
        y=np.array(np.absolute(((np.cos(0.2+arr)-np.cos(0.2-arr))/(2*arr))-((-1)*np.sin(0.2))), dtype=np.float32)

      
        plt.plot(arr,y)
        plt.ylabel('f(h) (error)')
        plt.xlabel('h')
        plt.yscale("log")
        plt.xscale("log")
        plt.show()
 


