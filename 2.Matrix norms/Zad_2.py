
import numpy as np

A1=np.array([[2.34332898, -0.11253278,-0.01485349, 0.33316649, 0.71319625],
    [-0.11253278, 1.67773628, -0.32678856, -0.31118836, -0.43342631],
    [-0.01485349, -0.32678856, 2.66011353, 0.85462464, 0.16698798],
    [0.33316649, -0.31118836, 0.85462464, 1.54788582, 0.32269197],
    [0.71319625, -0.43342631, 0.16698798, 0.32269197, 3.27093538]],dtype=np.float64)

A2=np.array([[2.34065520, -0.05353743, 0.00237792 ,0.32944082, 0.72776588],
    [-0.05353743, 0.37604149, -0.70698859 ,-0.22898376 ,-0.75489595],
    [0.00237792, -0.70698859 ,2.54906441, 0.87863502, 0.07309288],
    [0.32944082, -0.22898376 ,0.87863502 ,1.54269444, 0.34299341],
    [0.72776588 ,-0.75489595, 0.07309288, 0.34299341 ,3.19154447]],dtype=np.float64)



B1=np.transpose(np.array([3.55652063354463, -1.86337418741501, 5.84125684808554,-1.74587299057388, 0.84299677124244],dtype=np.float64))
B11=np.transpose(np.array([0.00001,0,0,0,0],dtype=np.float64))
B2=B1+B11
print("Dla rownania A1y=B")
y1=np.linalg.solve(A1,B1)
print(y1)
print("Dla rownania A1y'=B'")
y2=np.linalg.solve(A1,B2)
print(y2)

print("Norma euklidesowa 1:")
print(np.linalg.norm(y2-y1))

print("Dla rownania A2y'=B'")
y3=np.linalg.solve(A2,B2)
print(y3)
print("Dla rownania A2y=B")
y4=np.linalg.solve(A2,B1)
print(y4)

print("Norma euklidesowa 2:")
print(np.linalg.norm(y4-y3))

print("Wspolczynnik uwarunkowania  A1")
print(np.linalg.cond(A1))

print("Wspolczynnik uwarunkowania A2")
print(np.linalg.cond(A2))
