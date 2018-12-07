import numpy as np
import matplotlib.pyplot as plt
from numpy import fft as f
from scipy import interpolate as interp

#---------------------------------------------1Punto

data = np.loadtxt("derivada.txt")

#archivo = file("derivada.txt","r")
#linea1 = str(archivo.readlines())
#print (data)

dt = 0.01
def derivada(x):
	x_prime = (x[2:-1]-x[0:-3])/(2.0*dt)
	return x_prime

y = derivada(data)
x = []
for i in range(len(y)):
	x.append(0.0+(i*dt))

plt.figure()
plt.plot(x,y)

x = []
for i in range(len(data)):
	x.append(0.0+(i*dt))
plt.plot(x,data,c="r")
plt.legend(["derivada","funcion"])
plt.savefig("Derivada.png")
plt.close()

#---------------------------------------------2Punto

def funcion(x):
	return np.sin(x)**2
N = 10000 #muestreo cada 0.01s
x = np.linspace(0,10,N)
y = funcion(x)

plt.figure()
cuadro1 = plt.subplot(1,3,1)
cuadro1.plot(x,y,c="g")
plt.legend(["original"])

fourier = f.fft(y)
freq = f.fftfreq(len(y))

for i in range(len(freq)):
	if (freq[i]>1.0 and freq[i]<2.0):
		fourier[i] = 0.0		
	
#fourier[1.0<freq<2.0] = 0.0
cuadro2 = plt.subplot(1,3,2)
cuadro2.plot( f.fftshift(freq) , abs(f.fftshift(fourier)))
plt.legend(["fourier"])

inversa = f.ifft(fourier)
cuadro3 = plt.subplot(1,3,3)
cuadro3.plot(x,inversa , c="r")

plt.legend(["inversa"])
plt.savefig("Fourier.png")
plt.close()

#---------------------------------------------3Punto

def funcion(x):
	y=0.0
	#for i in range(len(x)):
	if (x >= 0.0):
		y= np.exp(-x)
	if (x < 0.0):
		y=0.0
	return y

pasos = 10000
lista=[]
lista.append(np.random.rand())

for i in range(pasos):
	siguiente =  lista[i] + np.random.normal()
	a2 = funcion(lista[i])
	a1 = funcion(siguiente)
	
	razon = a1/a2
	if (razon >=1.0):
		lista.append(siguiente)
	else:
		alfa = np.random.rand()
		if (razon > alfa):
			lista.append(siguiente)
		else:
			lista.append(lista[i])

plt.figure()
plt.hist(lista,100)
plt.title("histograma MCMC")
plt.savefig("expo.png")
plt.close()

#---------------------------------------------4Punto
c=1.0

x = np.linspace(0,100,100)
presente = np.ones((100,1))
futuro = np.ones((100,1))
#print ( len(presente) )

for i in range(100):
	presente[i] = 50.0
presente[0]=0.0
presente[99]=10.0

plt.figure()	 
K = 300
contador =1
for k in range(K):
	for j in range(1,99):
		futuro[j] = presente[j] + c*( presente[j-1] + presente[j+1] - 2*presente[j] )
	if(k%8 == 0.0):
		plt.subplot()
		plt.plot(x,futuro)
		texto = "temperatura VS posicion, t="+str(k) 
		plt.legend([texto])
		contador += 1
	presente = futuro
plt.show()
plt.savefig("Calor.png")



















