import numpy as np
class rectan:
	def __init__(self,x,y,a,c):
		self.centro=[x,y]
		self.lados=[a,c]

def comparar(rect1,rect2):
	if (rect1.centro == rect2.centro):
		if(rect1.lados == rect2.lados):
			print "los rectangulos se intersectan formando un rectangulo de lados",rect1.centro[0],"y",rect2.centro[1]
		elif(rect1.lados != rect2.lados):
			print "los rectangulos no se intersectan"
		elif(rect1.lados[0] == rect2.lados[0] or rect1.lados[1] == rect2.lados[1]):
			print "los rectangulos se intersectan formando un rectangulo de ancho o largo cero"



	elif (( np.absolute(rect1.centro[0] - rect2.centro[0]) > (rect1.lados[0]/2.0 + rect2.lados[0]/2.0) ) or (np.absolute(rect1.centro[1] - rect2.centro[1]) > (rect1.lados[1] + rect2.lados[1]))):
		if (( np.absolute(rect1.centro[0] - rect2.centro[0]) >(rect1.lados[0] + rect2.lados[0]) ) and (np.absolute(rect1.centro[1] - rect2.centro[1]) > (rect1.lados[1] + rect2.lados[1]))):
			print "los rectangulos no se intersectan"



	elif( (np.absolute(rect1.centro[0] - rect2.centro[0])== rect1.lados[0]/2.0 + rect2.lados[0]/2.0) or (np.absolute(rect1.centro[1] - rect2.centro[1])== rect1.lados[1]/2.0 + rect2.lados[1]/2.0)):

		if((np.absolute(rect1.centro[0] - rect2.centro[0])==rect1.lados[0]/2.0 + rect2.lados[0]/2.0) and (np.absolute(rect1.centro[1] - rect2.centro[1])==rect1.lados[1]/2.0 + rect2.lados[1]/2.0)):

			if(rect1.centro[0]>rect2.centro[0] and rect1.centro[1]>rect2.centro[1]):		
				print "los rectangulos se tocan en un solo punto de coordenadas", rect2.centro[0] + rect2.lados[0]/2.0 , rect2.centro[1] + rect2.lados[1]/2.0
			elif(rect1.centro[0]>rect2.centro[0] and rect1.centro[1]<rect2.centro[1]):		
				print "los rectangulos se tocan en un solo punto de coordenadas", rect2.centro[0] + rect2.lados[0]/2.0 , rect2.centro[1] - rect2.lados[1]/2.0
			elif(rect1.centro[0]<rect2.centro[0] and rect1.centro[1]<rect2.centro[1]):		
				print "los rectangulos se tocan en un solo punto de coordenadas", rect2.centro[0] - rect2.lados[0]/2.0 , rect2.centro[1] - rect1.lados[1]/2.0
			elif(rect1.centro[0]<rect2.centro[0] and rect1.centro[1]>rect2.centro[1]):		
				print "los rectangulos se tocan en un solo punto de coordenadas", rect1.centro[0] + rect1.lados[0]/2.0 , rect1.centro[1] - rect1.lados[1]/2.0

		elif((np.absolute(rect1.centro[0] - rect2.centro[0])==(rect1.lados[0]/2.0) + (rect2.lados[0]/2.0))):
			print "los rectangulos se intersectan formando un rectangulo de lados", "CERO", (rect1.lados[1]/2.0) + (rect2.lados[1]/2.0) - np.absolute(rect1.centro[1] - rect2.centro[1])
		else:
			print "Se intersectan en un borde de los rectangulos de tamanio", (rect1.lados[0]/2.0) + (rect2.lados[0]/2.0) - np.absolute(rect1.centro[0] - rect2.centro[0]) , "CERO"
		


	elif ( (np.absolute(rect1.centro[0] - rect2.centro[0]) < rect1.lados[0]/2.0 + rect2.lados[0]/2.0) and (np.absolute(rect1.centro[1] - rect2.centro[1]) < rect1.lados[1]/2.0 + rect2.lados[1]/2.0) ):
		if (np.absolute(rect1.centro[0]-rect1.lados[0]/2.0) < np.absolute(rect2.centro[0]-rect2.lados[0]/2.0) and rect1.centro[0]+rect1.lados[0]/2.0 > rect2.centro[0]+rect2.lados[0]/2.0):
			print "los rectangulos se intersectan formando un rectangulo de lados", rect2.lados[0], rect1.lados[1]/2.0 + rect2.lados[1]/2.0 - np.absolute(rect1.centro[1] - rect2.centro[1])
		elif (np.absolute(rect1.centro[0]-rect1.lados[0]/2.0) > np.absolute(rect2.centro[0]-rect2.lados[0]/2.0) and rect1.centro[0]+rect1.lados[0]/2.0 < rect2.centro[0]+rect2.lados[0]/2.0):
			print "los rectangulos se intersectan formando un rectangulo de lados", rect1.lados[0], rect1.lados[1]/2.0 + rect2.lados[1]/2.0 - np.absolute(rect1.centro[1] - rect2.centro[1])
		elif (np.absolute(rect1.centro[1]-rect1.lados[1]/2.0) < np.absolute(rect2.centro[1]-rect2.lados[1]/2.0) and rect1.centro[1]+rect1.lados[0]/2.0 > rect2.centro[0]+rect2.lados[1]/2.0):
			print "los rectangulos se intersectan formando un rectangulo de lados", rect1.lados[0]/2.0 + rect2.lados[0]/2.0 - np.absolute(rect1.centro[0] - rect2.centro[0]),rect2.lados[1]
		elif (np.absolute(rect1.centro[1]-rect1.lados[1]/2.0) > np.absolute(rect2.centro[1]-rect2.lados[1]/2.0) and rect1.centro[1]+rect1.lados[0]/2.0 < rect2.centro[0]+rect2.lados[1]/2.0):
			print "los rectangulos se intersectan formando un rectangulo de lados", rect1.lados[0]/2.0 + rect2.lados[0]/2.0 - np.absolute(rect1.centro[0] - rect2.centro[0]),rect1.lados[1]
		else:
			print "los rectangulos se intersectan formando un rectangulo de lados", rect1.lados[0]/2.0 + rect2.lados[0]/2.0 - np.absolute(rect1.centro[0] - rect2.centro[0]), rect1.lados[1]/2.0 + rect2.lados[1]/2.0 - np.absolute(rect1.centro[1] - rect2.centro[1])


#rectangulos que se variaron multiples veces para confirmar condicionales aniadidos		
#o1=rectan(2,2,4,4)
#o2=rectan(2,4,2,2)
#comparar(o1,o2)

