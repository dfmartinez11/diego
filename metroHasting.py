import matplotlib.pyplot as plt
import numpy as np

#for i in range(50):
#    print (np.random.normal(5.0,0.1))

def dobleG(x):
    return np.exp(-(x-1.0)**2 /0.5) + np.exp(-(x+1.0)**2 /0.5)

#def dobleG(x):
#    return np.exp(-(x)**2 /((x-4.0)**2 + 0.1)) 
x= np.linspace(-5,5,200)
y= dobleG(x)
plt.figure()
a1= plt.subplot(2,1,1)
a1.plot(x,y,c="r")
plt.legend(["gaussianas"])


N = 10000
puntos = np.empty((0))
x=np.random.normal(0.0,1.0)
for i in range(N):
    delta = np.random.normal()
    #print (delta)
    y1 = dobleG(x)
    y2 = dobleG(x+delta)
    
    aleat = np.random.rand()
    razon = y2/y1
    if(razon >= 1.0):
        puntos = np.append(puntos,x+delta)
        x = x + delta
    else:
        if(razon > aleat):
            puntos = np.append(puntos,x+delta)
            x = x + delta
        else:
            puntos = np.append(puntos,x)

#print (puntos)
#max = np.argmax( dobleG(puntos) )
#print (max)
#puntos2 = puntos/200
a2= plt.subplot(2,1,2)
a2.hist(puntos,100)  
plt.savefig("gaussiana.png")    
    

