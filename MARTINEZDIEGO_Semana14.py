import numpy as np
import matplotlib.pylab as plt
#######-------------------1

def f1(x, a , b):
	return (a*x) + (b*x) - (x**3)
# yi son los observados

def chi(yi , yg):
	suma = 0
	#for i in range(yi.shape()[0]):
	#	suma += (yi[i] - yg[i])**2
	for i in range(len(yi)):
		suma += (yi[i]-yg[i])*(yi[i]-yg[i])
	return suma

#######-------------------2

yobs = np.loadtxt("datos.txt")

yi = yobs.transpose()[1]
xi = yobs.transpose()[0]
plt.figure()
plt.plot(xi,yi, c="r")
plt.scatter(xi,yi, c="g")
plt.show()


a=[]
a.append(1)
b=[]
b.append(5)
prob=[]
print " "
print "Chi**2 de a,b = 1,1 es: ", chi(a,b)
prob.append(-np.exp(chi(a,b)))
#######-------------------3

N=2000

m=10000000
minimo=0
valorChi = 0
for i in range(N):
	b2 = b[i] + np.random.uniform(-0.5,0.5)	 
	a2 = a[i] + np.random.uniform(-0.5,0.5)
	m1 = np.exp(-chi(yi,f1(xi,b[i],a[i])))
	m2 = np.exp(-chi(yi,f1(xi,b2,a2)))
	al = m2/m1
	if al <1.0 :
		betha = np.random.normal()
		if (betha > a):
			a.append(a2)
			b.append(b2)
		else:
			a.append(a[i])
			b.append(b[i])
		
	else:
		a.append(a2)
		b.append(b2)
	if m1<m :
		minimo = i
		valorChi = m1

print "chi minimo esta en la posicion:", minimo, " y tiene valor de ", valorChi	
print " "
print "Mejores parametros= ","a: ", a[minimo], "b: ", b[minimo]


plt.scatter(a,b)
plt.show()

		
	





		
