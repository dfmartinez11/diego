import matplotlib.pyplot as plt
import numpy as np
from numpy import fft as f
from scipy import interpolate as interp
from scipy import interpolate as interp

N = 100
xobs = np.linspace(-5,5,N)
def func(x):
    return x**2 - x
yobs = func(xobs) + np.random.rand(N)
plt.figure()
v1 = plt.subplot(2,1,1)
v1.scatter(xobs, yobs, c="r")


def funcObs(x,a,b):
    return (a*x**2) - (b*x)

def chi(obs , y):
    chi = np.sum( (obs - y)*(obs - y) )
    return chi/(1.0*len(y))

proba = []
a=[]
b=[]

a.append(6.0)
b.append(-7.0)
proba.append(  np.exp(-chi(yobs , funcObs(xobs,a[0],b[0]))  )    )
#print (proba)

K = 100000
s=0.1
for i in range(0,K):
    a2 = a[i] + np.random.normal(a[i],s)
    b2 = b[i] + np.random.normal(b[i],s)  
    c1 = np.exp(-chi(yobs , funcObs(xobs,a[i],b[i])))
    c2 = np.exp(-chi(yobs , funcObs(xobs,a2,b2)))
    razon = c1/c2
    alfa = np.random.random()
    if(razon >= 1.0):
        a.append(a2)
        b.append(b2)
        proba.append( np.exp(-chi(yobs , funcObs(xobs,a2,b2))) )
    else:
        if(razon >= alfa):
            a.append(a2)
            b.append(b2)
            proba.append( np.exp(-chi(yobs , funcObs(xobs,a2,b2))) )
        else:
            a.append(a[i])
            b.append(b[i])
            proba.append( np.exp(-chi(yobs , funcObs(xobs,a[i],b[i]))) )

posicion = np.argmax(proba)
print ("parametros--- a=", a[posicion], " b=", b[posicion])
print ("probabilidad de parametros =", proba[posicion])
y = funcObs(xobs,a[posicion],b[posicion])
v1.plot(xobs,y, c="g")
plt.legend(["observados","parametro"])

v2 = plt.subplot(2,1,2)
v2.scatter(xobs, y)
v2.plot(xobs,func(xobs), c="g")
plt.legend(["parametros","real"])
plt.savefig("montecarloMethod.png")
