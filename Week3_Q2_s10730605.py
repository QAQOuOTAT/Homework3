# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:34:57 2024

@author: Student
"""
import random
print('Type x to Exit\n')
while True:
    i=input('Pleace input a min : ')
    if i =='x':
        print('Thanks for using\n')
        break
    b=int(input('Pleace input a max : '))
    n=int(input('Pleace input a Number : '))
    a=int(i)
    listR=[]
    while True:
        if n==0:
            break
        x=random.randint(a, b)
        listR.append(x)
        n=n-1
    listR.sort()
    print(listR)
    