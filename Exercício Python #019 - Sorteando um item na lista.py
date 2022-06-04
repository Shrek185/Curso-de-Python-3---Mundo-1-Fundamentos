"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de Python 3 - Mundo 1: Fundamentos (2022)

Exercício Python #019 - Sorteando um item na lista

https://www.youtube.com/watch?v=_Nk02-mfB5I&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=28

Um professor que sortear um dos seus quatro alunos para apagar o quadro.
faça uma programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

"""
from random import choice
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno:  '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno:   '))

lista = [n1, n2, n3, n4]

escolhido = choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))