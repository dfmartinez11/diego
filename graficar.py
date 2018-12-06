import numpy as np
import matplotlib.pyplot as plt
from numpy import fft as f




datos = np.loadtxt("datos.dat")
dato = np.loadtxt("difSencilla.dat")
datoss = np.loadtxt("difSencillaLeapF.dat")

x = datos.transpose()[0]
y = datos.transpose()[1]

a=plt.figure()
v1 = plt.subplot(3,2,1)
#plt.xlim(0,10)
v1.plot(x,y, color="r")
v1.plot(x,2*y +1, color ="g")
plt.legend(["original" , "aumentada"])

v2=plt.subplot(3,2,2)
#plt.xlim(0,15)
v2.plot(x,y+np.random.rand(len(y)), color ="b")


y = y + np.random.rand( len(y) )
fo = f.fftshift(f.fft(y))
x = f.fftshift(f.fftfreq( len(y) ))
#y[abs(x) > 0.1] = 0

fo[abs(x) > 0.0085] = 0

a1=plt.subplot(3,2,3)
a1.plot(x,abs(fo))
plt.legend(["fourier ODE"])

iy = f.ifft(fo)
a2 = plt.subplot(3,2,4)
a2.plot(x,iy, color="r")
#plt.xlim(0,0.1)
plt.legend(["inversa"])


dato = np.loadtxt("difSencillaRunge.dat")

v3 = plt.subplot(3,2,5)
v3.plot(dato.transpose()[0],dato.transpose()[1], color="b")
v3.plot(datos.transpose()[0],datos.transpose()[1], color="r")
#plt.xlim(0,0.1)
plt.legend(["Runge","Euler"])

v4 = plt.subplot(3,2,6)
v4.plot(dato.transpose()[0],dato.transpose()[1], color="b")
v4.plot(datoss.transpose()[0],datoss.transpose()[1], color="g")
#plt.xlim(0,0.1)
plt.legend(["Runge","LeapF"])


a.savefig("graficaCPP.png")


                       
                      
                      