import numpy as np
import matplotlib.pyplot as plt
import sys 

v=1.19592

#N=float(argv[1])
#Np=float(argv[2])
#a=float(argv[3])
#b=float(argv[4])

plt.figure()

x = np.linspace(0, 5*np.pi,1000)
def funcion (x):
	y = np.exp(-0.1*x) * np.sin(x)
	return y

plt.plot(x,funcion(x))
plt.show()


print ("Valor exacto: ", v)


x_posit=[]
y_posit=[]
x_negat=[]
y_negat=[]
for i in range(len(x)):
	if funcion(x[i]) >= 0:
		x_posit.append(x[i])
		y_posit.append(funcion(x[i]))
		x_negat.append(x[i])
		y_negat.append(0)
	else:
		x_negat.append(x[i])
		y_negat.append(funcion(x[i]))
		x_posit.append(x[i])
		y_posit.append(0)

plt.plot(x_posit , y_posit)
plt.plot(x_negat , y_negat)
plt.show()

	
x1 = np.random.rand(1000000) * (5*np.pi) 
y1 = np.random.rand(1000000) * (max(y_posit) - min(y_posit)) + min(y_posit)

x2 = np.random.rand(1000000) * (5*np.pi) 
y2 = np.random.rand(1000000) * (max(y_negat) - min(y_negat)) + min(y_negat)

#plt.scatter(x1,y1)
#plt.show()
#plt.scatter(x2,y2)
#plt.show()

f1 = funcion(x1) - y1
f_posit  = np.where(f1>0.0)
plt.scatter(x1[f_posit], y1[f_posit])
plt.show()

f2 = funcion(x2) - y2
f_negat  = np.where(f2<0.0)
plt.scatter(x2[f_negat], y2[f_negat])
plt.show()

intervalo1 = (max(y_posit)) * (5*np.pi)
intgr1 = intervalo1 * (np.size(f_posit))/(1.0*np.size(y1))

intervalo2 = (min(y_negat)) * (5*np.pi)
intgr2 = intervalo2 * (np.size(f_negat))/(1.0*np.size(y2))

integral = intgr1 + intgr2
print ("Por Monte Carlo es" , integral)








