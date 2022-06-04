'''
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de Python 3 - Mundo 1: Fundamentos (2022)

Faça um algoritmo que leia uma temperatura em graus celsius e transforme em fahrenheit

https://www.youtube.com/watch?v=9l_Gay8BuAw&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=22
'''
celcio = float(input('Informe a temperatura em C:'))
fahrenheit =  ((celcio * 1.8) + 32)
print('A temperatura de {:.1f}C coresponde a {:.1f}F.'. format(celcio, fahrenheit))