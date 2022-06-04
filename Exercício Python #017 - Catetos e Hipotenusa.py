"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de Python 3 - Mundo 1: Fundamentos (2022)

Exercício Python #017 - Catetos e Hipotenusa

https://www.youtube.com/watch?v=vmPW9iWsYkY&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=26

Faça um progrma que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
"""
'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co**2 + ca **2) ** (1/2)
print('A Hipotenusa vai medir {:.2f}'.format(hi))

'''

'''
import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A Hipotenusa vai medir {:.2f}'.format(hi))

'''
from math import hypot


co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A Hipotenusa vai medir {:.2f}'.format(hi))