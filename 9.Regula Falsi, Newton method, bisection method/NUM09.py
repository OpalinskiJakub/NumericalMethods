import numpy as np

import matplotlib.pyplot as plt
xPrzyblizoneBisekcji=[]
xPrzyblizoneFalsi=[]
xPrzyblizoneSieczne=[]
xPrzyblizoneNewtona=[]

iteration=[]


def f1(x):
    z=np.exp(x)-2
    return z
def f2(x):
    z=np.exp(x)-2
    z=z*z
    return z
    
def f3(x):
    z=np.exp(x)-2
    z=z*z*z
    return z

def f3f(x):
    z=np.exp(x)-2
    z=z*z*z
    y=3*np.exp(3*x)-12*np.exp(2*x)+12*np.exp(x)

    return z/y

def f1d(x):
    z=np.exp(x)
    return z
def f2d(x):
    z=2*np.exp(2*x)-4*np.exp(x)
    return z
    
def f3d(x):
    z=3*np.exp(3*x)-12*np.exp(2*x)+12*np.exp(x)
    return z


def metodaBisekcji(funkcja, x1, x2):
    kroki=1

    while abs(x2-x1)>1e-10:
        kroki=kroki+1
        x3=(x1+x2)/2
        add=np.abs(np.log(2)-x3)
        xPrzyblizoneBisekcji.append(add)
        if funkcja(x3) == 0:
            return x3
        elif funkcja(x1)*funkcja(x3)<0:
            x2=x3

        else:
            x1=x3
        

    
    x3=(x1+x2)/2
    print("Ilosc krokow")
    print(kroki)
    return x3


def metodaFalsi(funkcja,x1,x2):
    kroki=0

    while True:
        kroki=kroki+1
        x3a=funkcja(x1)*x2-funkcja(x2)*x1
        x3b=funkcja(x1)-funkcja(x2)
        x3=x3a/x3b
        add=np.abs(np.log(2)-x3)
        xPrzyblizoneFalsi.append(add)
        if funkcja(x3) == 0:
            print("Ilosc krokow")
            print(kroki)
            return x3
        
        elif funkcja(x3) * funkcja(x1) < 0:
            x2 = x3
        else:
            x1 = x3
        if np.abs(np.log(2)-x3)<1e-10:
            print("Ilosc krokow")
            print(kroki)
            return x3

    


def metodaSiecznych(funkcja,x1,x2):
    kroki=0

    while abs(x2-x1)>1e-10:
        kroki=kroki+1
        x3 = x2 - funkcja(x2) * (x2 - x1) / (funkcja(x2) - funkcja(x1))
        x1 = x2
        add=np.abs(np.log(2)-x1)
        xPrzyblizoneSieczne.append(add)
        x2 = x3

    print("Ilosc krokow")
    print(kroki)
    return x1


def mewtodaNewton(f, fd,x):
    kroki=0
    while abs(f(x)) >1e-10:
        kroki=kroki+1
        x = x - f(x) / fd(x)
        add=np.abs(np.log(2)-x)
        xPrzyblizoneNewtona.append(add)
    print("Ilosc krokow")
    print(kroki)
    return x




print(metodaBisekcji(f1,0,1))

print(metodaFalsi(f1,0,1))

print(metodaSiecznych(f1,0,1))

print(mewtodaNewton(f1,f1d,1))
for i in range (34):
    iteration.append(i)

while len(xPrzyblizoneBisekcji)<34:
    xPrzyblizoneBisekcji.append(0)

while len(xPrzyblizoneFalsi)<34:
    xPrzyblizoneFalsi.append(0)

while len(xPrzyblizoneSieczne)<34:
   xPrzyblizoneSieczne.append(0)

while len(xPrzyblizoneNewtona)<34:
    xPrzyblizoneNewtona.append(0)





plt.plot(iteration, xPrzyblizoneBisekcji, '.r-',markersize=10,label='Bisekcji')
plt.plot(iteration, xPrzyblizoneFalsi, '.b-',markersize=10,label='Falsi')

plt.plot(iteration, xPrzyblizoneSieczne, '.y-',markersize=10,label='Siecznych')
plt.plot(iteration, xPrzyblizoneNewtona, '.g-',markersize=10,label='Newtona')
plt.ylabel('|xi-x*|')
plt.xlabel('iteracje')
plt.legend()
plt.yscale('log') 
plt.show()
