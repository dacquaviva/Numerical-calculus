# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 15:14:32 2017

@author: casa
"""
import numpy as np

def fun(x):
    y=x**4-4    
   
    return y
    
    
def fun1(x):
    y=3*x**3-4

    return y   
    
tol = 0.0001
print"METODO DI NEWTON"
 
xn = 1.5
fxn=fun(xn)
trovato=False
if fxn != 0:
     precedente = xn
     for i in range(50):
                  fxn=fun(xn)
                  f1xn=fun1(xn)
                  xn = xn-(fxn/f1xn) #NEWTON
                  #xn = xn+fxn#DIVERGIAMO
                  #xn = xn-(fxn/11)#DIREZIONE COSTANTE
                  if abs(xn-precedente)<=tol:
                       print "iterate numero:",i
                       print "La radice x=",xn,"fx=",fxn
                       trovato=True
                       break
                  precedente = xn
                   
     if trovato==False: print("Il metodo di newton non converge")
         
         
         
    