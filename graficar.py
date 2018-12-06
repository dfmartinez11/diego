import numpy as np
import matplotlib.pyplot as plt
from numpy import fft as f




#datos = np.loadtxt("datos.dat")
datos = np.loadtxt("difSencilla.dat")

x = datos.transpose()[0]
y = datos.transpose()[1]

a=plt.figure()
v1 = plt.subplot(2,2,1)
#plt.xlim(0,10)
v1.plot(x,y, color="r")
v1.plot(x,2*y +1, color ="g")
plt.legend(["original" , "aumentada"])

v2=plt.subplot(2,2,2)
#plt.xlim(0,15)
v2.plot(x,y+np.random.rand(len(y)), color ="b")


y = y + np.random.rand( len(y) )
fo = f.fftshift(f.fft(y))
x = f.fftshift(f.fftfreq( len(y) ))
#y[abs(x) > 0.1] = 0

fo[abs(x) > 0.0085] = 0

a1=plt.subplot(2,2,3)
a1.plot(x,abs(fo))
plt.legend(["fourier ODE"])

iy = f.ifft(fo)
a2 = plt.subplot(2,2,4)
a2.plot(x,iy, color="r")
#plt.xlim(0,0.1)
plt.legend(["inversa"])

a.savefig("graficaCPP.png")


                       
                      
                      