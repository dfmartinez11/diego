import matplotlib.pyplot as plt
import numpy as np
from numpy import fft as f

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
v3.plot(xo[delta],abs(yo[delta]),label="filtradaFourier")
v3.plot(xo,abs(yo),label="filtradaFourier")
plt.legend()

v4 =plt.subplot(4,1,4)
#plt.xlim(-1.0,1.0)
v4.plot(x , f.ifft(yo) ,label="filtradaFuncion")

plt.legend()
plt.savefig("OtraFourier.png")



