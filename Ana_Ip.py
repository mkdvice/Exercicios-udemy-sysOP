# -*- coding: utf-8 -*-

__author__ = "@MkDVice"

ip = int(input('Digite os três primeiros digitos do IP: '))

if (ip >= 0) and (ip <= 127):
    print('Ip de classe A')
elif(ip >= 128) and (ip <= 191):
    print('Ip de classe B')
elif(ip >= 192) and (ip <= 223):
    print('Ip de classe C')
elif(ip >= 224) and (ip <= 239):
    print('Ip de classe D')
elif(ip > 240):
    print('Ip de classe E')