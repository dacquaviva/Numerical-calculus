# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:19:06 2017

@author: casa
"""

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

x = np.linspace(0,1,50)# x dei dati

y = 2*x + (np.random.rand(50))# y dei dati

A = np.asmatrix([ x, np.ones(50)])#creo matrice sistema sovradeterminato

A=A.T#Trasposta matrice per adattarla al sistema

b=np.asmatrix(y).T #Considero il vettore come una matrice in modo da poter fare la trasposta per adattarlo al sistema



#   QR
Q,R = la.qr(A) # Decomposizione QR della matrice A
Qb = np.dot(Q.T,b) # Moltiplicazione Q^T*b
coeff_qr = la.solve(R,Qb) # Risoluzione sistema lineare R*x = Q^T*b
coeff_qr=np.array(coeff_qr)#trasformo la matrice coeff_qr in un array in modo da consentire a python di eseguire i calcoli
retta = coeff_qr[0]*x+coeff_qr[1]#creao la retta
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
retta = coeff_pseudo[0]*x+coeff_pseudo[1]
print 'Soluzione con pseudo inversa '
print coeff_pseudo
plt.plot(x,retta,'m-',x,y,'go')
plt.show()



coeff_lstsq = la.lstsq(A,b)[0] #la funione lstsq mi restituisce i coefficenti colcolati in un sistema sovradeterminato 
coeff_lstsq=np.array(coeff_lstsq)
retta = coeff_lstsq[0]*x+coeff_lstsq[1]
print 'Soluzione con lstqs '
print coeff_lstsq
plt.plot(x,retta,'k-',x,y,'co')
plt.show()




