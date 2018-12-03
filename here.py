print ("I am here ready to make all easier tan it seems")
print ("  ")
import numpy as np
import matplotlib.pyplot as plt
from numpy import fft as f

dim = 8
tiempo = 4
dt=0.01
dx=1.0
c=dt/(dx*dx)

fut = np.ones((dim,dim))
pres = np.ones((dim,dim))
for i in range(dim):
    for j in range(dim):
        pres[i][j] = 2.0
for i in range(2,7): 
    pres[3][i] = 25.0

plt.figure()
for k in range(tiempo):
    for i in range(dim-1):
        for j in range(dim-1):
            fut[i][j] = pres[i][j] + c*(pres[i][j+1] + pres[i][j-1] + pres[i+1][j] + pres[i-1][j] -4*pres[i][j])
    
    plt.subplot(2,2,k+1)
    plt.pcolor(pres)
    plt.colorbar()
    texto = "calor"+str(k)+".png"
    #plt.title(texto)
    
    pres = fut.copy()
plt.savefig("evolucionCalor.png")
print ("How strange life shows itself to who is living")
        
    

