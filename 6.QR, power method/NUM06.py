import numpy as np


M=np.array([[3,6,6,9],[1, 4 ,0 ,9],[0, 0.2, 6, 12],[0, 0 ,0.1, 6]])
B=np.array([[3, 4, 2, 4],[4 ,7 ,1 ,(-3)],[2, 1, 3 ,2],[4, (-3), 2, 2]])


#print(np.linalg.eig(M))
#print(M)

while True:
    arr2=np.diag(M, -1)
    q, r = np.linalg.qr(M)
    M=np.dot(r,q)
    arr=np.diag(M, -1)
    if (np.linalg.norm(np.abs(arr-arr2))<10**-16):
        break

    



print("Podpunkt a)")
print("Wartosc wlasne")
for i in range(4):
    print(M[i][i])



x=np.array([1,0,0,0])

#print(np.linalg.eig(B))

while True:
    x1=x
    x=np.dot(B,x)
    eig=np.linalg.norm(x)
    x=x/eig
    if (np.linalg.norm(np.abs(x1-x))<10**-8):
        break

print("Podpunkt b)")
print("Wartosc wlasna")
print(eig)
print("Wektor wlasny:")
print(x)