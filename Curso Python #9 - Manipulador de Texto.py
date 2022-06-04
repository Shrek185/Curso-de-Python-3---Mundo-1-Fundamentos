"""
Autor : Douglas Nascimento (Shrek18.5)

Obs:    Curso Python - Curso Python #09 - Manipulando Texto - Curso em Video Gustavo Guanabara

        https://www.youtube.com/watch?v=a7DH88vk2Sk&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=31

"""
frase = 'Curso em Vídeo Python'
frase2 = '   Aprenda Python  '
# Fatiamento
print(frase[9])  # Mostra o nono character da frase
print(frase[9:13])  # Começa no 9 e mostra até o 12
print(frase[9:21])  # Começa no 9 e mostra até o 20
print(frase[9:21:2]) # Começa no 9 e mostra até o 20 saltando em 2 em 2
print(frase[:5])    #Onde vai começar : onde vai parar - começa no inicio e vai até 4
print(frase[15:])   #Do 15 até o final
print(frase[9::3])  #Começa no 9 e pula em 3 em 3

#Analise
print(len(frase))   #Mostra o tamanho da frase
print(frase.count('o')) #Contar quantas vezes aparece o 'o' minusculo.
print(frase.count('o', 0, 13))  #Vai contar do 0 ao 12 quantas letras 'o' vai aparece
print(frase.find('deo'))    #Achar a posição do 'deo'
print(frase.find('Android')) #Quando coloca uma frase que não existe na string ela mostra -1 isso significa que não existe nesta string
print('Curso' in frase) #Operador de verificar true or false

#Transformação
print(frase.replace('Python', 'Android')) #trca python por android
print(frase.upper())    #Tudo Maiusculo
print(frase.lower())    #TudoMinusculo
print(frase.capitalize())   #só a primeira letra fica maiusculo
print(frase.title())    #Analise palavra por palavra para cada primeira letra fique maiusculo
print(frase2.strip())   #Remove os espaço do começo e do final
print(frase2.rstrip())  #Remove os espaço do lado direito
print(frase2.lstrip())  #Remove os espaço do lado esquerdo

#Divisão
print(frase.split())    #divide a frase em cada espaço contando a cada separação gerando em varias listas

#Junção
print('-'.join(frase)) #Juntar a frase com - no lugar do espaço