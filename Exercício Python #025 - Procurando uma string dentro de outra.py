"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de Python 3 - Mundo 1: Fundamentos (2022)

https://www.youtube.com/watch?v=WHWGz2Dy1ZU&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=35

#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

"""
import time

nome = str(input('Qual é seu nome completo? ')).strip()
print('Analisando o seu nome...')
time_duration = 3
time.sleep(time_duration)
analisando = 'SILVA' in nome.upper()

if analisando == True:{
    print('Seu nome tem Silva!')
}
else:{
    print('Seu nome não tem Silva!')
}
