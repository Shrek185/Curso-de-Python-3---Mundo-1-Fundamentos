"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de Python 3 - Mundo 1: Fundamentos (2022)

https://www.youtube.com/watch?v=SifYYsXhLM8&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=37

#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.


"""

nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()
print('Muito prazer em tem conhecer {}!'.format(nome))
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu ultimo nome é {}'.format(n[len(n) - 1]))