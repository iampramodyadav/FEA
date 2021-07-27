from sympy import *
def SHAPE(p,z):
  '''
  SHAPE(p,z)
  p: order (p) of approximation
  z:value of natural coordinate
  This function return shape funtions values at given x
  note: x=symbols('x')
  '''
  z=Symbol('z')
  n=[]

  for i in range(0, p+1):
    point=-1
    point=point+2*i/p
    n.append(point)

  shape=[1]*(p+1)
  for i in range(0,p+1):
    for j in range(0,p+1):
      if i!=j:
        shape[i]=shape[i]*((z-n[j])/(n[i]-n[j]))
  return shape
