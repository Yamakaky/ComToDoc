#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import glob

def get_files(dir):
    """ Liste <dir> et renvoie la liste des .dasm qu'il contient (récursif) """
    liste = list()    # contient la liste les fichiers .dasm

    for file in glob.glob(dir + "/*"):
        if os.path.isdir(file):
            liste += get_files(file)
        elif os.path.splitext(file)[-1] == ".dasm":
            liste.append(file)

    assert len(liste) is not 0, "Le dossier ne contient pas de fichiers .dasm"
    return liste

def get_coms(file_list):
    """ Retourne la liste des lignes utilisées pour la doc """
    com_list = list()
    
    for file in file_list:
        for line in open(file, "r").read().splitlines(): # sans les \n
            if len(line) > 3 and line[:3] == ";;;": 
                com_list.append(line[3:])

    assert len(com_liste) is not 0, "Aucun commentaire détecté"
    return com_list
