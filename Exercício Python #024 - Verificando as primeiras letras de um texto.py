"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de Python 3 - Mundo 1: Fundamentos (2022)

https://www.youtube.com/watch?v=QroT8cZMRnc&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=34

#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

"""

cid = str(input('Em que cidade você nasceu? ')).strip()
analise = (cid[:5].upper() == 'SANTO')

if analise == True: {
    print('A sua cidede tem Santo no nome!')
}
else: {
    print('A sua cidade nào tem Santo no nome!')
}