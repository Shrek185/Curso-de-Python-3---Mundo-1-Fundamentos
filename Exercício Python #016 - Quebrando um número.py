"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de Python 3 - Mundo 1: Fundamentos (2022)

Exercício Python #016 - Quebrando um número

Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

https://www.youtube.com/watch?v=-iSbDpl5Jhw&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=25
"""

'''
from math import trunc

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))