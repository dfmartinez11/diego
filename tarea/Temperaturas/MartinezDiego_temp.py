import numpy as np
import matplotlib.pyplot as plt

ar = open("647_Global_Temperature_Data_File.txt" , "r")
x=ar.readlines()

anios =[]
anomalias=[]
anomaSuaves=[]
for i in range(len(x)):
	x2=x[i].split("\t")
	anios.append(x2[0])
	anomalias.append(x2[1])

aniosNP=np.array(anios)

anomaliasNP=np.array(anomalias)
plt.figure()
plt.plot(aniosNP,anomaliasNP)
plt.title("Anomalias temperatura en funcion del anio")
plt.savefig("Grafica_temp.pdf")

mayoresAcinco=[]
for i in range(anomaliasNP.size):
	if (float(anomalias[i]) > 0.5) :
		mayoresAcinco.append(anios[i])

anios2=anios
for j in range(len(mayoresAcinco)):
	anios2.remove(mayoresAcinco[j])
anomalias2 = anomalias[1:-(len(mayoresAcinco)+2)]
a2=anomalias2
maximo1=0
for i in range(len(anomalias2)):
	if float(anomalias2[i]) > maximo1 :
		maximo1=float(anomalias2[i])
anomalias2.remove(str(maximo1))

maximo2=0
for i in range(len(anomalias2)):
	if float(anomalias2[i]) > maximo2 :
		maximo2=float(anomalias2[i])

anios =[]
anomalias=[]
anomaSuaves=[]
for i in range(len(x)):
	x2=x[i].split("\t")
	anios.append(x2[0])
	anomalias.append(x2[1])
	anomaSuaves.append(x2[2])

a=str(anios[anomalias.index(str(maximo2))])
b=str(anios[anomalias.index(str(maximo1))])
mayoresAcinco.insert(0, a)
mayoresAcinco.insert(1, b)

aniosGrafica=mayoresAcinco

def ordenar():
	for i in range (len(mayoresAcinco)-1):
		a=anomalias[anios.index(mayoresAcinco[i])]
	
		if( (i+1) <= len(mayoresAcinco)):
			b=anomalias[anios.index(mayoresAcinco[i+1])]
			if(a>b):
				t=mayoresAcinco[i]
				mayoresAcinco[i]=mayoresAcinco[i+1]
				mayoresAcinco[i+1]=t
		if( (i-1) >= 0 ):
			c=anomalias[anios.index(mayoresAcinco[i-1])]
			if(a<c):
				t=mayoresAcinco[i]
				mayoresAcinco[i]=mayoresAcinco[i-1]
				mayoresAcinco[i-1]=t
ordenar()
ordenar()
ordenar()
ordenar()
ordenar()
ordenar()
ordenar()
masCali = mayoresAcinco	
print masCali	
	
valoresCal=[]
for i in range(20):
	valoresCal.append(anomalias[anios.index(aniosGrafica[i])])

AnomaSuaves=[]
for i in range(len(anomaSuaves)):
	x2=anomaSuaves[i].split("\r")	
	AnomaSuaves.append(x2[0])
AnomaSuavesNP=np.array(AnomaSuaves)

plt.figure()
plt.plot(aniosNP,AnomaSuavesNP)
plt.scatter(mayoresAcinco, valoresCal)
plt.plot(aniosGrafica, valoresCal)
plt.title("Anomalias Suaves de temperatura en funcion del anio")
plt.savefig("Grafica_temp2.pdf")








	

    
