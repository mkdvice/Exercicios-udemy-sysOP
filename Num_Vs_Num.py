# -*- coding: utf-8 -*-

__author__ = "@MkDVice"

print('Bem Vindo! Ao combate de números. Que o maior número ganhe!\n')

num1 = input('Digite o primeiro número: ')  # entrada da primeira váriavel
num2 = input('Digite o segundo número: ')   # entrada da segunda váriavel

'''Condição para mostrar o resultado da dispusta de números '''

if(num1 > num2):
    print('\nO {} venceu! Ele é maior que {}'.format(num1, num2)) # imprime a vitória do num1
elif(num1 < num2):
    print('\nO {} venceu! Ele é maior que {}'.format(num2, num1)) # imprime a vitória do num2
else:
    print('\nEmpate! Os dois valores são iguais') # imprime empate
