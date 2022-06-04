'''
Escreva um prorama que  leia um valor em metros e o exiba convertido em centímetros e milímetros.
km hm dam m dm cm mm

Faça um programa que leia um número inteiro qualquer a sua tabuada.

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
Considere US$1,00 = R$3,27.

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

Faça um algoritmo que leia o salario de um funcionário e mostre o seu novo salário, com 15% de aumento.
'''
n1 = float(input('Digite um valor em (m): '))
km = n1 * 0.001
hm = n1 * 0.01
dam = n1 * 0.1
m = n1
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000


print(' O valor digitado em km é {:.3f} \n'.format(km))
print(' O valor digitado em hm é {:.3f} \n'.format(hm))
print(' O valor digitado em dam é {:.3f} \n'.format(dam))
print(' O valor digitado em m é {:.3f} \n'.format(m))
print(' O valor digitado em dm é {:.3f} \n'.format(dm))
print(' O valor digitado em cm é {:.3f} \n'.format(cm))
print(' O valor digitado em mm é {:.3f} \n'.format(mm))
