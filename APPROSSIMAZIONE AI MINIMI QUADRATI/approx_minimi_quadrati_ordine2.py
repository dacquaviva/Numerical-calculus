# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 14:33:50 2017

@author: casa
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:19:06 2017

@author: casa
"""

import numpy as np
import numpy.linalg as la
from numpy import ones
import matplotlib.pyplot as plt

x = np.linspace(0,1,50)# x dei dati

y = 3*x**2+ 2*x +2*x**3 +(np.random.rand(50))# y dei dati

A = np.asmatrix([ x**2,x, ones(50)])#creo matrice sistema sovradeterminato

A=A.T#Trasposta matrice per adattarla al sistema

b=np.asmatrix(y).T #Considero il vettore come una matrice in modo da poter fare la trasposta per adattarlo al sistema




Q,R = la.qr(A) # Decomposizione QR della matrice A
Qb = np.dot(Q.T,b) # Moltiplicazione Q^T*b
coeff_qr = la.solve(R,Qb) # Risoluzione sistema lineare R*x = Q^T*b
coeff_qr=np.array(coeff_qr)
retta = coeff_qr[0]*x**2+coeff_qr[1]*x+coeff_qr[2]
print 'Soluzione fattorizzazione QR '
print coeff_qr
plt.plot(x,retta,'r-',x,y,'yo')
plt.show()
plt.cla()


#pseudo-inversa
pseudo_A=la.inv(A.T*A)*A.T
coeff_pseudo=pseudo_A*b
coeff_pseudo=np.array(coeff_pseudo)
#coeff_pseudo_inv=la.pinv(A)*b
retta = coeff_pseudo[0]*x**2+coeff_pseudo[1]*x+coeff_pseudo[2]
print 'Soluzione con pseudo inversa '
print coeff_pseudo
plt.plot(x,retta,'m-',x,y,'go')
plt.show()


coeff_lstsq = la.lstsq(A,b)[0] # computing the numpy solution
coeff_lstsq=np.array(coeff_lstsq)
retta = coeff_lstsq[0]*x**2+coeff_lstsq[1]*x+coeff_lstsq[2]
print 'Soluzione con lstqs '
print coeff_lstsq
plt.plot(x,retta,'k-',x,y,'co')
plt.show()

