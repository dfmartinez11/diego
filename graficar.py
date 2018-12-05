import numpy as np
import matplotlib.pyplot as plt
from numpy import fft as f

datos = np.loadtxt("datos.dat")
x = datos.transpose()[0]
y = datos.transpose()[1]

a=plt.figure()
v1 = plt.subplot(1,2,1)
#plt.xlim(0,10)
v1.plot(x,y, color="r")
v1.plot(x,2*y +1, color ="g")

v2=plt.subplot(1,2,2)
#plt.xlim(0,15)
v2.plot(x,y+np.random.rand(len(y)), color ="b")

a.savefig("graficaCPP.png")