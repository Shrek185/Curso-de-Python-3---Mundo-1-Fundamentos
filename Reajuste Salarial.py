'''
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso Curso de Python 3 - Mundo 1: Fundamentos (2022)

https://www.youtube.com/watch?v=cTkivN8XcJ0&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=21

Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.
'''
salario = float(input('Qual é o salário do funcionário? R$ '))
dicidio =  salario * 0.15
novosalario = salario + dicidio
print('Um funcionario que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}.'. format(salario, novosalario))