#!/usr/bin/python3
# -*- coding: utf-8 -*-

def replace(text, char_1, char_2):
    """
    pre: 'text' is the string to modify
         'char_1' is the word/character to be modified
         'char_2' is the word/chararcter to replace 'ids'
    post: return the modified string

    """
    a = list(text) #Casts the text as a list since strings are immuable
    i = 0 #Sets the index to zero
    while i<(len(text)-len(char_1))+1: #Optimises the number of indetation
        if a[i:i+len(char_1)] == list(char_1): #Checks the equality
            a[i:i+len(char_1)] = char_2 #If its's true therefore we change the
            i+=len(char_1) #We add the length of the char_1 cause we just checked the equality for the next chqr_1 length caracters
        else:
            i+=1 #We increase the i by 1

    t = '' #Since we casted the text into a list now we have to cast back into a string
    for l in a:
        t+=l
    return t


