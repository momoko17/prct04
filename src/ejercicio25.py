#!/usr/bin/python
#!encoding: UTF-8

from math import sqrt

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
c = float(raw_input('Valor de c: '))
if a == 0:
  if b == 0:
    if c == 0:
      print 'La ecuacion no tiene solucion'
    else:
      print 'La ecuacion tiene infinitas soluciones'
  else:
    x = -c / b
    print 'La solucion de la ecuacion es: x=%4.3f' % x
else:
  x1 = (-b + sqrt(b**2 - 4*(a*c))) / (2 * a)
  x2 = (-b - sqrt(b**2 - 4*(a*c))) / (2 * a)
  print 'Las soluciones de la ecuacion son: x1=%4.3f y x2=%4.3f' % (x1, x2)
#La condicion del "c" esta mal. En el 24 te piden las que no se hacen 0 y en el 25 te estan pidiendo que sean igual a 0