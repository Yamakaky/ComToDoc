#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Fonction:
    """ Cette classe regroupe les commentaires d'une fonction en un
    objet.
    m_nom
    m_description
    m_args : tableau associatif 'registre : description'
    """
    
    def __init__(self, nom='', description='', args=None):
        """ args est un tableau associatif """
        self.m_nom = nom
        self.m_description = description
        if args is None:
            args = dict()
        self.m_args = args

    def getHTML(self):
        """ Retourne un string en HTML de l'objet """
        html = "<section>"
        html += "<h1>" + self.m_nom + "</h1>"
        html += "<p>" + self.m_description + "</p>"
        html += "<dl>"
        for key in self.m_args:
            html += "<dt>" + key + "</dt>"
            html += "<dd>" + self.m_args[key] + "</dd>"
        html += "</dl>"
        html += "</section>"
        return html

    def match(commentaires):
        listeFonctions = list()
        current = None
        
        for line in commentaires:

            if line[:8] == "FONCTION":
                if not current is None:
                    listeFonctions.append(current)
                current = Fonction(nom=line[9:])

            elif line[:11] == "DESCRIPTION":
                current.m_description = line[12:]

            elif line[:3] == "ARG":
                liste = str.split(line[4:], " ", 1)
                current.m_args[liste[0]] = liste[1]

        if not current is None:
            listeFonctions.append(current)

        return listeFonctions
