
"""
Created on Sun Jan 15 04:19:54 2017

@author: daniele
"""

import numpy as np
 
     
     
def lu(A):
    
    n = len(A)
    P = np.eye(n)
    L=np.asmatrix([[0.0]*n for i in range(n)])#'''Creo L '''
    
    U = np.asmatrix([[0.0]*n for i in range(n)])#'''Creao U'''
    i=0
   
    while (np.allclose(A, np.triu(A))==False):
      index=np.argmax(abs(A[i:n,i]))   #'''Pivoting parziale'''  
      P[[i,index+i],:]=P[[index+i,i],:]  #''''Creo matrice di permutazione'''
      A[[i,index+i],:]=A[[index+i,i],:]  # inverto righe matrice A'''
      L[[i,index+i],:]=L[[index+i,i],:]  #inverto righe matrice L

      
      L[i+1:n,i]=(np.matrix(A[i+1:n,i]/A[i,i]))#"""calcolo L21"""
      A[i+1:n,i+1:n]=A[i+1:n,i+1:n]-L[i+1:n,i]*A[i,i+1:n] #"""calcolo U22"""
      A[i+1:n,i]=0#"""azzero colonna sotto il pivot"""
      i=i+1;
    L=L+np.eye(n)
     
    return (L, A, P)
  

a = np.asmatrix([[4.,0.,1.,1.],[3.,1.,3.,1.],[0.,1.,2.,0.],[2.,2.,4.,1.]])
A = np.asmatrix([[4.,0.,1.,1.],[3.,1.,3.,1.],[0.,1.,2.,0.],[2.,2.,4.,1.]])
#c = np.asmatrix([[-1.,6.,-4.],[0.5,1.,5.],[2.,-4.,2.]])
#c = np.asmatrix([[1.,2.],[3.,1.]])
L,U,P= lu(a)

print "P*A:"
print(P*A)
print "L*U:"
print(L*U)
