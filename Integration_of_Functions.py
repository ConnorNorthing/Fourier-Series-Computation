# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sympy as sp

n,t = sp.symbols({'n','t'})

x_t = t

#simplify is used to factorise the function
a0 = sp.simplify((2/(10*sp.pi))*sp.integrate(x_t, (t,0,sp.pi)))
sp.pprint(a0)
print('\n')

#simplify is used to factorise the function
bn = sp.simplify((2/2)*sp.integrate(x_t * sp.sin((sp.pi)*n*t), (t,-1,1)))
sp.pprint(bn)
