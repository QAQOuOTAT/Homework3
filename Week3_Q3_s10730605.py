# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:48:01 2024

@author: Student
"""
import random
suits=['H','D','S','C']
ranks=['A','2','3','4','5','6','7','8','9','10','K','Q','J' ]
deck=[(rank,suit)for suit in suits for rank in ranks]
random.shuffle(deck)
sets=[deck[i::4]for i in range(4)]
for i, cardset in enumerate(sets):
    cardset.sort()
    print(f"Set{i+1}:{cardset}")