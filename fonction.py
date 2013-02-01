#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Fonction:
    """ Cette classe regroupe les commentaires d'une fonction en un
    objet.
    nom
    description
    args : tableau associatif 'registre : description'
    """
    
    def __init__(self, nom='', description='', args=None):
        """ args est un tableau associatif """
        self.nom = nom
        self.description = description
        if not args:   # args vide
            args = dict()
        self.args = args

    def match(commentaires):
        listeFonctions = list()
        current = None
        
        for line in commentaires:

            if line[:8] == "FONCTION":
                if current: # non None
                    listeFonctions.append(current)
                current = Fonction(nom=line[9:])

            elif line[:11] == "DESCRIPTION":
                current.description = line[12:]

            elif line[:3] == "ARG":
                liste = str.split(line[4:], " ", 1)
                current.args[liste[0]] = liste[1]

        if current: #not None
            listeFonctions.append(current)

        return listeFonctions
