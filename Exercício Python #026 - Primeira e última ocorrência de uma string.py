"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de Python 3 - Mundo 1: Fundamentos (2022)

https://www.youtube.com/watch?v=23UOVEetNPY&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=36

#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

"""
import time

frase = str(input('Digite uma frase: ')).upper().strip()
print('Analisando a sua frase...')
time_duration = 3
time.sleep(time_duration)
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A') + 1))
print('A ulitma letra "A" apareceu na posição {}'.format(frase.rfind('A') + 1))
