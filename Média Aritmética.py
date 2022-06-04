'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.

Escreva um prorama que  leia um valor em metros e o exiba convertido em centímetros e milímetros.

Faça um programa que leia um número inteiro qualquer a sua tabuada.

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
Considere US$1,00 = R$3,27.

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

Faça um algoritmo que leia o salario de um funcionário e mostre o seu novo salário, com 15% de aumento.
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = ((n1 + n2)/2)

print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'. format(n1, n2, m))
