# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 17:39:21 2017

@author: casa
"""
import numpy as np
def fun(x):
    #y = x**2 - 3
    #y = x**3 - x - 1
    #y = x - np.exp(-x**2)
    y=x**4-4    
    #y=3*x**4-11*x**3-21*x**2+99*x-54     
    return y
    
    
def fun1(x):
    #y = 2*x
    #y = 3*x**2 - 1
    #y = 1 + 2 * np.exp(-x**2) * x
    y=3*x**3-4
    #y= 12*x**3-33*x**2-42*x+99
    return y   
tol = 0.0001
print"METODO DI NEWTON IN RELAZIONE CON I PUNTI FISSI"


print"METODO DIREZIONE COSTANTE" 
xn = 1.5
fxn=fun(xn)
trovato=False
if fxn != 0:
     precedente = xn
     for i in range(50):
                  fxn=fun(xn)
                  xn = xn-(fxn/11)
                  if abs(xn-precedente)<=tol:
                       print "iterate numero:",i
                       print "La radice x=",xn,"fx=",fxn
                       trovato=True
                       break
                  precedente = xn
                   
     if trovato==False: print("Il metodo della direzione costante non converge")
      
      
    
print"METODO DELLA FALSA POSIZIONE"
 
xn = 1.5
xo=1.5
f1xo=fun1(xo)
fxn=fun(xn)
trovato=False
if fxn != 0:
     precedente = xn
     for i in range(50):
                  fxn=fun(xn)
                  xn = xn-(fxn/f1xo)
                  if abs(xn-precedente)<=tol:
                       print "iterate numero:",i
                       print "La radice x=",xn,"fx=",fxn
                       trovato=True
                       break
                  precedente = xn
                   
     if trovato==False: print("Il metodo della falsa posizione non converge")
         
         

print"METODO DELLE SECANTI"
 

precedente=1
xn=1.5
fxn=fun(xn)
fxnp=fun(precedente)
trovato=False
if fxn or fxnp != 0:
     for i in range(50):
                  fxn=fun(xn)
                  fxnp=fun(precedente)
                  dfn=(xn-precedente)/(fxn-fxnp)
                  aux = xn-(fxn*dfn)
                  if abs(aux-xn)<=tol:
                       print "iterate numero:",i
                       print "La radice x=",aux,"fx=",fun(aux)
                       trovato=True
                       break
                  precedente=xn
                  xn=aux
                   
     if trovato==False: print("Il metodo delle secanti non converge")