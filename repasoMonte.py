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
v1 = plt.subplot(3,1,1)
v1.plot(xobs, yobs, c="r")


def funcObs(x,a,b):
    return (a*x**2) - (b*x)

def chi(obs , y):
    chi = np.sum( (obs - y)*(obs - y) )
    return chi #/(1.0*len(y))

proba = []
a=[]
b=[]

a.append(6.0)
b.append(-7.0)
proba.append(  np.exp(-chi(yobs , funcObs(xobs,a[0],b[0]))  )    )
#print (proba)

K = 20000
s=0.55
for i in range(0,K):
    a2 = a[i] + np.random.uniform(-1,1)
    b2 = b[i] + np.random.uniform(-1,1)  
    c1 = -chi(yobs , funcObs(xobs,a[i],b[i]))
    c2 = -chi(yobs , funcObs(xobs,a2,b2))
    razon = c2/c1
    #print (razon)
    alfa = np.random.random()
    if(razon < 1.0):
        a.append(a2)
        b.append(b2)
        proba.append( np.exp(-chi(yobs , funcObs(xobs,a2,b2))) )
    else:
        if(razon < alfa):
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
v1.scatter(xobs,y, c="g")
plt.legend(["observados","parametro"])

v2 = plt.subplot(3,1,2)
v2.scatter(xobs, y)
v2.plot(xobs,func(xobs), c="r")
plt.legend(["parametros","real"])

v3 = plt.subplot(3,1,3)
v3.scatter(a, b)
plt.legend(["parametros a VS b"])
plt.savefig("montecarloMethod.png")

#print ("PARAMETROS")
#print(a)
#print(b)

