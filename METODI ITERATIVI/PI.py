# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 13:51:22 2017

@author: casa
"""

import numpy as np
from decimal import *
getcontext().prec= 10000# numero(n) cifre decimali
a=Decimal(1)#considera uno come 1.00000000000....(n cifre decimali)
b=Decimal(1/np.sqrt(Decimal(2)))
t=Decimal(0.25)
p = Decimal(1)
pi=None
while 1:
    x = Decimal((a+b)/2)
    y = Decimal(np.sqrt(a*b))
    t = Decimal(t - p*(a-x)*(a-x))
    a = Decimal(x)
    b = Decimal(y)
    p =Decimal(2*p)
    precedente = pi
    pi = Decimal(((a+b)*(a+b))/(4*t))
    if pi == precedente:
      break
   
print(pi)
