# -*- coding: utf-8 -*-

__author__ = "@MkDVice"

num1 = int(input('Digite um número: ')) # Lendo váriavel

'''Verificando o resto da divisão por 2, se = 0 é par, se não é Ímpar '''

if (num1 % 2 == 0):
    print('O número é par')
else:
    print('O número é Ímpar')

''' Verificando se é maior, igual ou menor que zero '''

if (num1 == 0):
    print('Esse número é Zero')
elif (num1 > 0):
    print('Esse número é positivo')
else:
    print('Esse número é negativo')