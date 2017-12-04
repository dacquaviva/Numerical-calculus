# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 15:02:39 2017

@author: casa
"""

import numpy as np
def fun(x):
    y = x**2 - 3
    #y = x**3 - x - 1
    #y = x - np.exp(-x**2)   
    return y
    
    
def fun1(x):
    y = 2*x
    #y = 3*x**2 - 1
    #y = 1 + 2 * np.exp(-x**2) * x
    return y   
    
tol = 0.0001
a = 0.
b = 4.

fa = fun(a) 
fb = fun(b)

n= int(np.log2(b-a)-np.log2(tol))
print"METODO DELLE BISEZIONI"
i=0
if fa*fb > 0:
    print "Nell'intervallo considerato la funzione non presenta nessuna radice."
else:
    c= (float(a)+b)/2
    fc = fun(c)
    while abs(fc) > tol:
         c= (float(a)+b)/2
         fc = fun(c)
        
         print "iterata numero: ",i
         print"a:", a, "    fa:", fa
         print"b:",b,"    fb:", fb  
         print"c:",c,"    fc:", fc
         
         if fa*fc<0:
            b=c
            fb=fc
         else:
             a=c
             fa=fc
         
         i=i+1
    print "La radice x=",c,"fx=",fc   
 
 
print"METODO DI NEWTON"
 
xn = 1.5
fxn=fun(xn)
trovato=False
if fxn != 0:
     precedente = xn
     for i in range(50):
                  fxn=fun(xn)
                  f1xn=fun1(xn)
                  xn = xn-(fxn/f1xn)
                  if abs(xn-precedente)<=tol:
                       print "iterate numero:",i
                       print "La radice x=",xn,"fx=",fxn
                       trovato=True
                       break
                  precedente = xn
                   
     if trovato==False: print("Il metodo di newton non converge") 
	           