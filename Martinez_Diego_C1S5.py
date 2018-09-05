import numpy as np

#

y1=[1,12,3]
y2=[3,3,5]
y3=[3,1,2]

A = np.array([y1,y2,y3])

#A[:1]=A[:1]+(-3*A[:0])
#print A.shape

A[1]= A[1]-(A[0]/A[0][0])*A[1]
#print A

A[2]= A[2]-(A[2][0])*A[0]
#print A

A[2]= A[2]-(A[1]/A[1][1])*A[2]
#print A


y1=[1,12,3]
y2=[3,3,5]
y3=[3,1,2]
A = np.array([y1,y2,y3])

#for j in range(0,A.shape[1]):
for i in range(1,A.shape[0]):
	A[i]=A[i]-(A[i-(i-1)]/A[i-1][0])*A[i]
print A





