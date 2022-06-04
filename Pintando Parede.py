'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

Faça um algoritmo que leia o salario de um funcionário e mostre o seu novo salário, com 15% de aumento.
'''
largura = float(input('Largura da parede em (m): '))
altura  = float(input('Altura da parede em (m): '))
area = largura * altura
tinta = area / 2
print("Sua parede tem a dimensão de {:.2f}m x {:.2f}m e a sua você área é de {:.2f}m².".format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.2f} l de tinta.'.format(tinta))