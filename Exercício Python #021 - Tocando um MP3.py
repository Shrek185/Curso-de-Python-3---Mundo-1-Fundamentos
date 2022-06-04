"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de Python 3 - Mundo 1: Fundamentos (2022)

Exercício Python #021 - Tocando um MP3

https://www.youtube.com/watch?v=9FiEji_fzvk&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=30

Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

"""
import pygame
pygame.init()
pygame.mixer.music.load('Track-06.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()