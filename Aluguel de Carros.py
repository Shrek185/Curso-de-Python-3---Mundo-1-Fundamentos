'''
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso Curso de Python 3 - Mundo 1: Fundamentos (2022)

Exercício Python #015 - Aluguel de Carros

Escreva um programa que pergunte a quantidade de de Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$0.15 por Km rodado.

https://www.youtube.com/watch?v=I4NYUeetLAc&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=23

'''
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}.'.format(pago))