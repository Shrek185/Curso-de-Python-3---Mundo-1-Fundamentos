"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de Python 3 - Mundo 1: Fundamentos (2022)

https://www.youtube.com/watch?v=wD2aerLMBWA&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=33

#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

"""

num = int(input('Informe um número: '))
u = num // 1 %10
d = num // 10 %10
c = num // 100 %10
m = num // 1000 %10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))