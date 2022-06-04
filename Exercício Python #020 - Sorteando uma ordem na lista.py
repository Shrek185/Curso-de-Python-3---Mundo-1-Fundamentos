"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de Python 3 - Mundo 1: Fundamentos (2022)

Exercício Python #020 - Sorteando uma ordem na lista

https://www.youtube.com/watch?v=OPh0nngbBSY&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=29

O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome quatro alunos e mostre a ordem sorteada.

"""
from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno:  '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno:   '))

lista = [n1, n2, n3, n4]

shuffle(lista)

print('A ondem de apresentação será')
print(lista)