# -*- coding: utf-8 -*-

import datetime

__author__ = "@MkDVice"

print('Análise de idade.\n')

ano = datetime.date.today().year  # definindo o ano atual pela biblioteca datetime
nasc = int(input('Qual é o ano de seu nascimento? ')) # entrada do ano de nascimento
idade = (ano - nasc)    # cálculo de idade

''' Condição para mostar se a pessoa é adulta (maior que 18 anos de idade) ou não adulta '''

if(idade >= 18):
    print('\nA pessoa é adulta')
else:
    print('\nA pessoa não é adulta')

