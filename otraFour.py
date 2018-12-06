import matplotlib.pyplot as plt
import numpy as np
from numpy import fft as f
from scipy import interpolate as interp

x1 = np.linspace(0,6,10)
y1 = np.sin(x1)
plt.figure()
v1 = plt.subplot(2,1,1)
v1.scatter(x1,y1)
y =  interp.interp1d(x1,y1)
x= np.linspace(0,6,1000)
v1.plot(x,y(x), c="g")
plt.legend(["datos", "lineal"])

v2 = plt.subplot(2,1,2)
v2.scatter(x1,y1)
y =  interp.interp1d(x1,y1, kind = "cubic")
x = np.linspace(0,6,1000)
v2.plot(x,y(x), c="r")
plt.legend(["datos", "cubica"])
plt.savefig("interp.png")



n=100
x= np.linspace(0,2*3.14,n)
y = np.sin(x) +np.random.rand(n)
yo = f.fftshift( f.fft(y) )
xo = f.fftshift( f.fftfreq(n) )

plt.figure()
v1 =plt.subplot(4,1,1)
v1.plot(xo,abs(yo),label="fourier")
plt.legend()

v2 =plt.subplot(4,1,2)
v2.plot(x,y,label="funcion")
plt.legend()

yo[abs(xo) > 0.01] = 0
#delta = np.where(abs(xo) > 0)

v3 =plt.subplot(4,1,3)
plt.xlim(-1.0,1.0)
#v3.plot(xo[delta],abs(yo[delta]),label="filtradaFourier")
v3.plot(xo,abs(yo),label="filtradaFourier")
plt.legend()

v4 =plt.subplot(4,1,4)
#plt.xlim(-1.0,1.0)
v4.plot(x , f.ifft(yo) ,label="filtradaFuncion")

plt.legend()
plt.savefig("OtraFourier.png")



