#!/usr/bin/python
#!encoding: UTF-8

numero = int( raw_input('Introduzca un numero '))
for potencia in [2,3,4,5]:
  print '%d elevado a %d es %d' % (numero, potencia, numero**potencia)
#El programa te eleva el numero que das a los cuatro numeros que estas dados en el for.