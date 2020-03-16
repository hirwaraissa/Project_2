#!/usr/bin/python3
# -*- coding: utf-8 -*-

def replace(text, char_1, char_2):
    """
    pre: 'text' is the string to modify
         'char_1' is the word/character to be modified
         'char_2' is the word/chararcter to replace 'ids'
    post: return the modified string

    """
    a = list(text)
    i = 0
    while i<(len(text)-len(char_1))+1:
        print(i)
        if a[i:i+len(char_1)] == list(char_1):
            a[i:i+len(char_1)] = char_2
            i+=len(char_1)
        else:
            i+=1
    t = ''
    for l in a:
        t+=l
    return t

