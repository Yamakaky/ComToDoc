#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import glob

def getFiles(dir):
    """ Liste <dir> et renvoie la liste des .dasm qu'il contient (récursif) """
    liste = list()    # contient la liste les fichiers .dasm

    for file in glob.glob(dir + "/*"):
        if os.path.isdir(file):
            liste += getFiles(file)
        elif os.path.splitext(file)[-1] == ".dasm":
            liste.append(file)
    return liste

def getComs(fileList):
    """ Retourne la liste des lignes utilisées pour la doc """
    comList = list()
    
    for file in fileList:
        for line in open(file, "r").read().splitlines(): # sans les \n
            if len(line) > 3 and line[:3] == ";;;": 
                comList.append(line[3:])

    return comList
