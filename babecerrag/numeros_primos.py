# -*- coding: utf-8 -*-
"""NUMEROS PRIMOS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qaQFLdUIQMYBdQRB2oeWPh_gZbQi7CGO
"""

def primo(n):
  if n==1:
    return False
  for x in range (2, n):
    if n % x ==0:
      return False
  return True

cant=0
n=2
limite=float(input("escribir la cantidad de numeros primos que quieres ver en la pantalla:  "))

while limite > cant:
  if primo(n) :
    cant +=1
    print(cant, n)

  n +=1

