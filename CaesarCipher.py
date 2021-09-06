# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 04:07:48 2021

@author: juanc
"""

def caesarCipher(s, k):
    while k > 26:
        k-=26
    alph=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    ALPH=[x.upper() for x in alph]
    for x in s:
        if x in alph:
            b=int((alph.index(x)))+k
            if b>25:
                b-=26
                print(alph[b],end="")
            else:
                print(alph[b],end="")
        elif x in ALPH:
            b=int((ALPH.index(x)))+k
            if b>25:
                b-=26
                print(ALPH[b],end="")
            else:
                print(ALPH[b],end="")
        else:
                print(x,end="")
if __name__ == '__main__':

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

