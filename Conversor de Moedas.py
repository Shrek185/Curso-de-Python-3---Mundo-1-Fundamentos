'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
Considere US$1,00 = R$3,27.

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

Faça um algoritmo que leia o salario de um funcionário e mostre o seu novo salário, com 15% de aumento.
'''
real = float(input('Quanto você tem de dinheiro na carteira R$ '))
dolar = real / 4.98
print("Com R$ {:.2f} você pode comprar US$ {:.2f}.".format(real, dolar))