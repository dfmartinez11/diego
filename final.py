import numpy as np
import matplotlib.pylab as plt

#######-------------------1

def f1(x, a , b):
	return (a*x*x) + (b*x)

def func(x):
    return 3.0*x*x - 4.0*x
    #return 3.0*x

def funcRuido(x):
    x = x + np.random.rand(len(x))
    return 3.0*x*x - 4.0*x

def chi(yi , yg):
	suma = 0
	#for i in range(yi.shape()[0]):
	#	suma += (yi[i] - yg[i])**2
	for i in range(len(yi)):
		suma += (yi[i]-yg[i])*(yi[i]-yg[i])
	return suma/len(yi)

#######-------------------2

x= np.linspace(0,20 ,60)
yobs = funcRuido(x)
yreal = func(x)

#yi = yobs.transpose()[1]
#xi = yobs.transpose()[0]
plt.figure()
plt.plot(x,yreal, c="r" , label="real")
plt.plot(x,yobs, c="b" , label="observado")
#plt.scatter(xi,yi, c="g")


######-----------------------------------------------------------------------------
a=[]
a.append(1.0)
b=[]
b.append(-2.0)
prob=[]
print (" ")
print ("Chi**2 de a,b = 1,1 es: ", chi(a,b) )
prob.append(-np.exp(chi(a,b)))

#######-------------------3

N=20000

m=10000000
minimo=0
valorChi = 10000
for i in range(N):
    b2 = b[i] + np.random.uniform(-0.5,0.5)	 
	a2 = a[i] + np.random.uniform(-0.5,0.5)
	m1 = np.exp(-chi(yreal,f1(x,a[i],b[i])))
	m2 = np.exp(-chi(yreal,f1(x,a2,b2)))
	al = m2/m1
	if al <1.0 :
		betha = np.random.normal()
		if (betha <= al):
            #prob.append(np.exp(-chi(yreal,f1(x,a2,b2))))
			a.append(a2)
			b.append(b2)
                        
		else:
            #prob.append(np.exp(-chi(yreal,f1(x,a[i],b[i]))))
			a.append(a[i])
			b.append(b[i])
	else:
        #prob.append(np.exp(-chi(yreal,f1(x,a2,b2))))
		a.append(a2)
		b.append(b2)
    if(m1<m):
        m=m1
        minimo=i
     

	
print ("chi minimo esta en la posicion:", minimo, " y tiene valor de ", valorChi)	
print ("   ")
print ("Mejores parametros= ","a: ", a[minimo], "b: ", b[minimo])

plt.scatter(x, f1(x,a[minimo],b[minimo]), label ="parametros")
plt.legend()
plt.savefig("curvaReal.png")

plt.figure()
plt.scatter(a,b)
plt.title("parametros a VS b")
plt.savefig("RandomPrametros.png")







