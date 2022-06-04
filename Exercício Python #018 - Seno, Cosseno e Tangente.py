"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de Python 3 - Mundo 1: Fundamentos (2022)

Exercício Python #018 - Seno, Cosseno e Tangente

https://www.youtube.com/watch?v=9GvsphwW26k&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=27

Faça um programa que leia um ângulo qualquer e mostre na tela o calor do seno, cosseno e
tangante desse ângulo

"""
from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'. format(an, seno))
cosseno = cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'. format(an, cosseno))
tangente = tan(radians(an))
print('O ângulo de {} tem o TANGENTE de {:.2f}'. format(an, tangente))