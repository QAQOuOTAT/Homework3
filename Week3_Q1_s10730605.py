# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print('Type x to Exit\n')
while True:
    a=str(input('Pleace input a Eng Name : '))
    if a == 'x':
        print('Thanks for using\n')
        break
    b=a.upper()
    dictA={a:b}
    print(dictA)