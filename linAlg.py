print ("I am here ready to make all easier tan it seems")
import numpy as np
import matplotlib.pyplot as plt
from numpy import fft as f

a = np.empty([2,2])
for i in range(2):
    for j in range(2):
        a[i][j] = np.random.rand() *2
vect = np.array([[2.2],[1.3]])

aT = np.linalg.inv(a)
producto = np.matmul(aT,a)
print (aT)
print (producto)
print (" ")

sol = np.linalg.solve(a,vect)
print ("SOLUCION" , sol)
print (np.matmul(a,sol))
print ("VECTOR")
print (vect)
print (" ")
       
eigVect = np.linalg.eig(a)[1]
eigVal = np.linalg.eig(a)[0]
print (eigVal)

proyeccionesVect = np.matmul(a, eigVect[0])
print(proyeccionesVect)

plt.figure()
plt.plot([0.0 , a[0][0]],[0.0 , a[0][1]])
plt.plot([0.0 , a[1][0]],[0.0 , a[1][1]])
plt.plot([0.0,eigVect[0][0]] , [0.0 , eigVect[0][1]] , label="eigVect")
plt.legend()
#plt.scatter(eigVect[1][0],eigVect[1][1])
plt.savefig("vectoresPoy.png")
       