import numpy as np
#Coloco nuevamente el reconocimiento del algoritmo con una matriz especifica

y1=[4,12,13]
y2=[3,30,55]
y3=[38,12,2]
A = np.array([y1,y2,y3])
#segunda fila
A[1]= A[1]-(A[0]/A[0][0])*A[1]
#tercera fila
A[2]= A[2]-(A[0]/A[0][0])*A[2]
#Nuevo pivote y trabajar en la tercera fila
A[2]= A[2]-(A[1]/A[1][1])*A[2]


y1=[4,12,1]
y2=[3,30,55]
y3=[38,12,6]
A = np.array([y1,y2,y3])


# primer recorrido por todas las filas de la primera columna

#	for i in range(1,A.shape[0]):
#		A[i]=A[i]-(A[0]/A[0][0])*A[i]
#	print A



# 1 Tratar de aniadir el otro for por columnas

# 	for j in range(0,A.shape[0]):
# 		for i in range(1,A.shape[0]):
#			A[i]=A[i]-(A[j]/A[j][j])*A[i]
#	print A

# Aniadir un inicio del range que pueda modificarse, el inicio del reange en j se deja constante

#	n=1
#	for j in range(0,A.shape[0]):
#		for i in range(n,A.shape[0]):
#		A[i]=A[i]-(A[j]/(A[j][j])*A[i]
#		n+=1
#	print A


# Como para algunas matrices se anula alguna fila , debe ser por hacer una divicion con enteros, colco entonces un 1.0* en la division
n=1
for j in range(0,A.shape[0]):
	for i in range(n,A.shape[0]):
		A[i]=A[i]-(A[j]/(1.0*A[j][j]))*A[i]
	n+=1
print A

#El BONO
#Se hizo prueba con matrices 2x2 , 3x3 para solucionar el sistema homogeneo.
#A continuacion mostramos como obtener la solucion en cualquier sistema con soluciones no infinitas.

y1=[1.5,2.1,1,1]
y2=[3,30,55,7]
y3=[38,12,6,3]
#El ultimo numero en cada lista corresponde a una componente del vector no homogeneo

A = np.array([y1,y2,y3])
n=1
for j in range(0,A.shape[0]):
	for i in range(n,A.shape[0]):
		A[i]=A[i]-((1.0*A[j]/(1.0*A[j][j]))*A[i])
	n+=1
print A

#Empieza  a solucionar de abajo hacia arriba
SolX3 = A[-1][-1]/(1.0*A[-1][-2])
print "variable 3 =", SolX3

#Para solucionar segunda variable se necesita restar dos elementos de la fila
A[-2][-2]=A[-2][-2]*SolX3
SolX2 = (A[-2][-1]-A[-2][-2])/(1.0*A[-2][-3])
print "variable 2 =",SolX2

#en la 3 variable se necesita restar tres elementos de la fila 
A[-3][-2]=A[-3][-2]*SolX3
A[-3][-3]=A[-3][-3]*SolX2
SolX1 = (A[-3][-1]-A[-3][-2]-A[-3][-3])/(1.0*A[-3][-3])
print "variable 1 =",SolX1






