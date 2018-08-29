import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def integral(funcion, menor, mayor, n ):
	

	listaX = np.linspace(menor, mayor, n) 
        listaY = funcion(listaX)
        
        listaY[-1]= listaY[-1] * 0.5
        listaY[0]= listaY[0] * 0.5
        
        dx = (mayor - menor) / (1.0*n)
                
	return sum(listaY) * dx
	#return dx


#def integralT(funcion, menor, mayor, error):

	#n=0
	#integral = 10000
	#t = 1000
	#while t < error:
		#n+=1
		#integral = (funcion, menor, mayor, n )
		#t = integral - integrate.trapz(funcion(x) , x )
	#return integral   


def xAlaSiete(lista):
    return lista**7

x7 = np.linspace(-10, 10, 10000)
plt.figure()
plt.plot( x7 , xAlaSiete(x7) )
plt.show()

print ("la integral de seno entre 0 y pi es: ", integral(np.sin,0,np.pi,200))
print ("la integral de x**7 es : ", integral(xAlaSiete,0,1,200))

#def grafica():
#	for n in range(100)
