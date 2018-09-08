import numpy as np
#centro1=[x1,y1]
#centro2=[x2,y2]

#lados1=[a1,c1]
#lados2=[a2,c2]

class rectan:
	def __init__(self,xK,yK,aK,cK):
		self.centro=[xK,yK]
		self.lados=[aK,cK]
def comparar(rect1,rect2):
	if (rect1.centro == rect2.centro):
		if(rect1.lados == rect2.lados):
			print "Se intercectan formando un rectangulo de lados",rect1.centro[0],"y",rect2.centro[1]
		#elif(rect1.lados != rect2.lados):
	if (( np.absolute(rect1.centro[0] - rect2.centro[0]) > np.absolute(rect1.lados[0] + rect2.lados[0]) ) or (np.absolute(rect1.centro[1] - rect2.centro[1]) > (rect1.lados[1] + rect2.lados[1]))):
		if (( np.absolute(rect1.centro[0] - rect2.centro[0]) > np.absolute(rect1.lados[0] + rect2.lados[0]) ) and (np.absolute(rect1.centro[1] - rect2.centro[1]) > (rect1.lados[1] + rect2.lados[1]))):
			print "No se intersectan de ningun modo"
		if ( (np.absolute(rect1.centro[0] - rect2.centro[0]) < np.absolute(rect1.lados[0] + rect2.lados[0])) or (np.absolute(rect1.centro[1] - rect2.centro[1]) < (rect1.lados[1] + rect2.lados[1])) ):
			print "Se intercectan en una linea"
		
		
o1=rectan(100,100,1,1)
o2=rectan(1,1,1,1)


comparar(o1,o2)

#lados1=[1,1]
#lados2=[1,1]

#if (centro1==centro2):
	#if(lados1==lados2):
		#print "son el mismo"


