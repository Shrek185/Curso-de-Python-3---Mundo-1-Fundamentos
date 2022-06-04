'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

Faça um algoritmo que leia o salario de um funcionário e mostre o seu novo salário, com 15% de aumento.
'''
preco = float(input('Qual é o preço do produto? R$ '))
desconto =  preco * 0.05
precodesconto = preco - desconto
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}'. format(preco, precodesconto))