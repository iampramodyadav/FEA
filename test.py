
from sympy import *
import numpy as np

def Legendre(n,x):
  """
  n: Order of polynomial
  x: Variable
  This function print Legendre polynomial of order n
  """

  x=symbols('x')
  if (n==0):
    return x*0+1.0
  elif (n==1):
    return x
  else:
    return ((2.0*n-1.0)*x*Legendre(n-1,x)-(n-1)*Legendre(n-2,x))/n