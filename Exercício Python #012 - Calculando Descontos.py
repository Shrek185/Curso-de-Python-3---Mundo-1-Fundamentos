"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso Curso de Python 3 - Mundo 1: Fundamentos (2022)

https://www.youtube.com/watch?v=4MAmKOT9FeU&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=20

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
"""
preco = float(input('Qual o preço do produto? R$ '))
novo = preco - (preco * 5/100)
print("O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}".format(
    preco, novo))