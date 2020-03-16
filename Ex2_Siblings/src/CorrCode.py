#!/usr/bin/python3
# -*- coding: utf-8 -*-
def siblings(filename):
    """
    pre:  - filename   : le nom du fichier,
    post: - Si la liste n'est pas vide, la foction retourne la liste des prénoms et ages ( dans un tuple) en
            ordre croissant des ages
            Si la list est vide, la fonction doit retourner "La liste est vide"
            Si le contenu de la liste est dans le mauvais format, la fonction retourne "Le fichier contient des erreurs et donc ne peut pas être lu"
            Si le fichier n'existe pas, la fonction doit lever un FileNotFoundError
    """
    HasNoSiblingsError = ValueError
    try:
        with open(filename,"r") as file:
            lst=file.readlines()  #Lecture du fichier
    except FileNotFoundError:
        raise FileNotFoundError
    
    if len(lst)>0:
        tab=[]    
        for line in lst:
            if "!" in line:
                tab.append(line.strip("\n").split("!"))  #Suppression des "!" et des "\n"
            else:
                return "Le fichier contient des erreurs et donc ne peut pas être lu."
        
        for i in range(len(tab)):
            for pers in range(len(tab)-1):           #Arrange les personnes dans l'ordre croissant
                if int(tab[pers][2])>int(tab[pers+1][2]):
                    tempo=tab[pers]
                    tab[pers]=tab[pers+1]
                    tab[pers+1]=tempo
        age=[] 
        for i in range (len(tab)):
            age.append((tab[i][1],tab[i][2]))     #Ajoute le nom et l'age de chacun (dans un tuple) dans la liste
        return age
    else:
        return HasNoSiblingsError
