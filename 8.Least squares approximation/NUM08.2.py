import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 60, 1)

print(x)
yresult=[]
for i in x:
    q=np.log10(i)
    w=34*np.sin(i)
    r=i*1
    yresult.append(q+w+r+np.random.normal(0.0,4.3))
yresult = np.array(yresult)

    


A = np.transpose(np.vstack([np.log10(x), np.sin(x),x]))


firstPart=np.dot(np.transpose(A),A)
secondPart=np.dot(np.transpose(A),yresult)
res=np.linalg.solve(firstPart,secondPart)


print(res)
yResultEnd=[]
for i in x:
    yResultEnd.append(res[0]*np.log10(i) + res[1]*np.sin(i) + i*res[2])

plt.plot(x, yresult, "o",markersize=5)
plt.plot(x, yResultEnd,'red')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
