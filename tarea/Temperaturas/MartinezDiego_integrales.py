import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.integrate import quad
import math

def cos(x):
	return np.cos(x)

def intCos(inferior,superior):
	return np.sin(superior)-np.sin(inferior)

def trapezoide(funcion,limInferior,limSuperior,cantidadPuntos):
	
	lista = np.linspace(limInferior,limSuperior,cantidadPuntos)
	
	delta = (limSuperior-limInferior)/(1.0*cantidadPuntos)
	listaY = funcion(lista)

	y = listaY
	listaY[0] = y[0]/2.0
	listaY[-1] = y[-1]/2.0

	n = 0.0
	for i in range(listaY.size):
		n+= listaY[i] * delta
	return n


def simpson(funcion,limInferior,limSuperior,cantidadPuntos):

	lista = np.linspace(limInferior,limSuperior,cantidadPuntos)
	delta = (limSuperior-limInferior)/(1.0*cantidadPuntos)
	listaY = funcion(lista)
	
	listaY = listaY*(4/3.0)
	listaY[0] = listaY[0]/4.0
	listaY[-1] = listaY[-1]/4.0
	
	listaY[2] = listaY[2]/2.0
	listaY[-3] = listaY[-3]/2.0

	integral=0.0
	for i in range(listaY.size):
		integral += listaY[i] * delta

	return integral


def monteCarlo(funcion,limInferior,limSuperior,cantidadPuntos):

	maximoX = np.linspace(limInferior,limSuperior,cantidadPuntos)
	maximoY = funcion(maximoX)

	maximo = 0.0
	for i in range(maximoY.size):
		if(maximoY[i]>maximo):
			maximo=maximoY[i]

	minimo =  100000000000.0
	for i in range(maximoY.size):
		if(maximoY[i]<minimo):
			minimo=maximoY[i]

	aleatoriosX = np.random.rand(cantidadPuntos)
	aleatoriosY = np.random.rand(cantidadPuntos)

	listaX = (aleatoriosX*(limSuperior-limInferior)) + limInferior
	listaY = (aleatoriosY*(maximo-minimo)) + minimo
	maximoY = funcion(listaX)	

#	implementacion del np.where()	
	LISTAY=listaY
	k = 0
	for i in range(maximoY.size):
		if(maximoY[i]-LISTAY[i] < 0.0):
			listaX=np.delete(listaX,i-k)
			listaY=np.delete(listaY,i-k)
			k+=1
		
	areatotal = (limSuperior-limInferior)*(maximo-minimo)*1.0
	razon = listaY.size / (1.0*LISTAY.size)
	return areatotal * razon

def valorMedio(funcion,limInferior,limSuperior,cantidadPuntos):
	
	valoresX = np.linspace(limInferior,limSuperior,cantidadPuntos)
	valoresY = funcion(valoresX)
	sumatoria=0.0

	for i in range(valoresY.size):
		sumatoria += valoresY[i] 
	intervalo = limSuperior - limInferior
	integral = (intervalo/cantidadPuntos)*sumatoria

	return integral

def montecarloNegativas(funcion,limInferior,limSuperior,cantidadPuntos):
	
	x = np.linspace(limInferior,limSuperior,cantidadPuntos)
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
	maximo1 = 0.0
	for i in range(len(y_posit)):
		if(y_posit[i]>maximo1):
			maximo1=y_posit[i]
	minimo1 =  100000000000.0
	for i in range(len(y_posit)):
		if(y_posit[i]<minimo1):
			minimo1=y_posit[i]
	maximo2 = 0.0
	for i in range(len(y_negat)):
		if(y_negat[i]>maximo2):
			maximo2=y_negat[i]

	minimo2 =  100000000000.0
	for i in range(len(y_negat)):
		if(y_negat[i]<minimo2):
			minimo2=y_negat[i]

	x1 = (np.random.rand(cantidadPuntos) * (1.0*(limSuperior-limInferior))) + limInferior
	y1 = np.random.rand(cantidadPuntos) * (1.0*(maximo1 - minimo1)) + minimo1

	x2 = (np.random.rand(cantidadPuntos) * (1.0*(limSuperior-limInferior))) + limInferior 
	y2 = np.random.rand(cantidadPuntos) * (1.0*(maximo2 - minimo2)) + minimo2

	f_posit  = np.where(funcion(x1) - y1 > 0.0)
	f_negat  = np.where(funcion(x2) - y2 < 0.0)
	
	areatotal1 = maximo1 * (limSuperior-limInferior)
	intgr1 = areatotal1 * (np.size(f_posit))/(1.0*np.size(y1))

	areatotal2 = minimo2 * (limSuperior-limInferior)
	intgr2 = areatotal2 * (np.size(f_negat))/(1.0*np.size(y2))

	return intgr1 + intgr2
	

def error(funcion,limInferior,limSuperior,cantidadPuntos):

	y=[trapezoide(funcion,limInferior,limSuperior,cantidadPuntos),simpson(funcion,limInferior,limSuperior,cantidadPuntos),montecarloNegativas(funcion,limInferior,limSuperior,cantidadPuntos),valorMedio(funcion,limInferior,limSuperior,cantidadPuntos)]

	valor = quad(funcion,limInferior, limSuperior)[0]
	for i in range(len(y)):
		y[i] = np.absolute(valor-y[i]) / (1.0*valor)
	return y
	

print "valor exacto = " , intCos(-(np.pi)/2.0,np.pi)
print "trapezoide: ", trapezoide(cos,-(np.pi)/2.0,np.pi,10001) , "," , error(cos,-(np.pi)/2.0,np.pi,10001)[0] 
print "simpson:    ", simpson(cos,-(np.pi)/2.0,np.pi,10001) , "," , error(cos,-(np.pi)/2.0,np.pi,10001)[1] 
print "montecarlo: ", montecarloNegativas(cos,-(np.pi)/2.0,np.pi,10001) , "," , error(cos,-(np.pi)/2.0,np.pi,10001)[2] 
print "valor med:  ", valorMedio(cos,-(np.pi)/2.0,np.pi,10001) , "," , error(cos,-(np.pi)/2.0,np.pi,10001)[3] 

plt.figure()
plt.title("Error de integracion Vs numero de puntos")
plt.ylabel("error En potencias de 10")
plt.xlabel("numero de puntos En potencias de 10")

x=np.logspace(2,7,6) + 1
X=[]
for i in range(6):
	X.append(math.log(x[i],10))

for j in range(4):
	errores = []
	for i in range(6):
		m = int(x[i])
		elemento = error(cos, -(np.pi)/2.0, np.pi, m)[j]
		errores.append( math.log(elemento,10) )
	if(j==0):
		plt.plot(X,errores,label="Trapezoides")
	elif(j==1):
		plt.plot(X,errores,label="Simpson")
	elif(j==2):
		plt.plot(X,errores,label="Montecarlo")
	else:
		plt.plot(X,errores,label="Valor Medio")

plt.savefig("MartinezDiego_int_error.pdf")
plt.close()



def Funcion(x):
	return 1/(np.sin(x)**(0.5))

x = np.linspace(0,1,1000)
y = Funcion(x)

print "La integral con singularidad vale", trapezoide(Funcion,0,1,10001), "con el metodo del Trapezoide con Simpson", simpson(Funcion,0,1,10001) ,"con Monte Carlo", montecarloNegativas(Funcion,0,1,10001),"y", valorMedio(Funcion,0,1,10001) ,"con Valores Medios"


def Strapezoide(cantidadPuntos):
	lista = np.linspace(0,1,cantidadPuntos)
	delta = 1/(1.0*cantidadPuntos)
	listaY = Funcion(lista)
	y = listaY
	listaY[0] = (10**6)/2.0
	listaY[-1] = y[-1]/2.0
	n = 0.0
	for i in range(listaY.size):
		n+= listaY[i] * delta
	return n

def Ssimpson(cantidadPuntos):
	lista = np.linspace(0,1,cantidadPuntos)
	delta = 1/(1.0*cantidadPuntos)
	listaY = Funcion(lista)
	listaY = listaY*(4/3.0)
	listaY[0] = (10**6)/4.0
	listaY[-1] = listaY[-1]/4.0
	listaY[2] = listaY[2]/2.0
	listaY[-3] = listaY[-3]/2.0
	integral=0.0
	for i in range(listaY.size):
		integral += listaY[i] * delta
	return integral

def SvalorMedio(cantidadPuntos):
	valoresX = np.linspace(0,1,cantidadPuntos)
	valoresY = Funcion(valoresX)
	valoresY[0] = 10**6
	sumatoria=0.0
	for i in range(valoresY.size):
		sumatoria += valoresY[i] 
	integral = sumatoria/cantidadPuntos
	return integral

def SmontecarloNegativas(Puntos):
	x = np.linspace(0,1,Puntos)
	x_posit=[]
	y_posit=[]
	x_negat=[]
	y_negat=[]
	for i in range(len(x)):
		if Funcion(x[i]) >= 0:
			x_posit.append(x[i])
			y_posit.append(Funcion(x[i]))
			x_negat.append(x[i])
			y_negat.append(0)
		else:
			x_negat.append(x[i])
			y_negat.append(Funcion(x[i]))
			x_posit.append(x[i])
			y_posit.append(0)
	y_posit[0]=10
	x1 = (np.random.rand(Puntos))
	y1 = np.random.rand(Puntos) * (0.1*(max(y_posit)-min(y_posit))) + min(y_posit)
	x2 = (np.random.rand(Puntos))
	y2 = np.random.rand(Puntos) * (0.1*(max(y_negat)-min(y_negat))) + min(y_negat)
	f_posit  = np.where(Funcion(x1) - y1 > 0.0)
	f_negat  = np.where(Funcion(x2) - y2 < 0.0)
	areatotal1 = max(y_posit) 
	intgr1 = areatotal1 * (np.size(f_posit))/(1.0*np.size(y1))
	areatotal2 = min(y_negat) 
	intgr2 = areatotal2 * (np.size(f_negat))/(1.0*np.size(y2))
	return intgr1 + intgr2

print "            "
print "El nuevo valor de la integral cambiando infinito por 10**6 es con --Simpson", Ssimpson(10001),"--Trapezoide:", Strapezoide(10001),"--Valor Medio:", SvalorMedio(10001),"--Montecarlo:", SmontecarloNegativas(10001)


def Strapezoide(Funcion,cantidadPuntos):
	lista = np.linspace(0,1,cantidadPuntos)
	lista[0]=10**(-6)
	delta = 1/(1.0*cantidadPuntos)
	listaY = Funcion(lista)
	y = listaY
	listaY[0] = listaY[0]/2.0
	listaY[-1] = y[-1]/2.0
	n = 0.0
	for i in range(listaY.size):
		n+= listaY[i] * delta
	return n

def Ssimpson(Funcion,cantidadPuntos):
	lista = np.linspace(0,1,cantidadPuntos)
	delta = 1/(1.0*cantidadPuntos)
	lista[0]=10**(-6)
	listaY = Funcion(lista)
	listaY = listaY*(4/3.0)
	listaY[0] = listaY[0]/4.0
	listaY[-1] = listaY[-1]/4.0
	listaY[2] = listaY[2]/2.0
	listaY[-3] = listaY[-3]/2.0
	integral=0.0
	for i in range(listaY.size):
		integral += listaY[i] * delta
	return integral

def SvalorMedio(Funcion,cantidadPuntos):
	valoresX = np.linspace(0,1,cantidadPuntos)
	valoresX[0] =10**(-6)
	valoresY = Funcion(valoresX)
	sumatoria=0.0
	for i in range(valoresY.size):
		sumatoria += valoresY[i] 
	integral = sumatoria/cantidadPuntos
	return integral

def SmontecarloNegativas(Funcion,Puntos):
	x = np.linspace(0,1,Puntos)
	x[0]=10**(-6)
	x_posit=[]
	y_posit=[]
	x_negat=[]
	y_negat=[]
	for i in range(len(x)):
		if Funcion(x[i]) >= 0:
			x_posit.append(x[i])
			y_posit.append(Funcion(x[i]))
			x_negat.append(x[i])
			y_negat.append(0)
		else:
			x_negat.append(x[i])
			y_negat.append(Funcion(x[i]))
			x_posit.append(x[i])
			y_posit.append(0)
	x1 = (np.random.rand(Puntos))
	y1 = np.random.rand(Puntos) * (0.1*(max(y_posit)-min(y_posit))) + min(y_posit)
	x2 = (np.random.rand(Puntos))
	y2 = np.random.rand(Puntos) * (0.1*(max(y_negat)-min(y_negat))) + min(y_negat)
	f_posit  = np.where(Funcion(x1) - y1 > 0.0)
	f_negat  = np.where(Funcion(x2) - y2 < 0.0)
	areatotal1 = max(y_posit) 
	intgr1 = areatotal1 * (np.size(f_posit))/(1.0*np.size(y1))
	areatotal2 = min(y_negat) 
	intgr2 = areatotal2 * (np.size(f_negat))/(1.0*np.size(y2))
	return intgr1 + intgr2
print "                "
print "El nuevo valor de la integral evaluando la funcion en 10**-6 y no en cero es --Simpson", Ssimpson(Funcion,10001),"--Trapezoide:", Strapezoide(Funcion,10001),"--Valor Medio:", SvalorMedio(Funcion,10001),"--Montecarlo:", SmontecarloNegativas(Funcion,10001)


def integralApoyo():
	return -(1**(0.5))

def funcionApoyo(x):
	return 1/((np.sin(x))**(0.5)) - 1/((x)**(0.5))

valor = 2.03480532
print "                "
print "Restando la singularidad el resultado es -- Simpson", Ssimpson(funcionApoyo,10001)+integralApoyo(), "--metodo del Trapezoide:", Strapezoide(funcionApoyo,10001)+integralApoyo() ,"--Monte Carlo:", SmontecarloNegativas(funcionApoyo,10001)+integralApoyo(), "--ValoresMedios:", SvalorMedio(funcionApoyo,10001)+integralApoyo()
print "                "
print "El metodo que mas se acerca es el de evaluar la funcion en 10**-6 y no en cero,  como se puede confirmar arriba"











