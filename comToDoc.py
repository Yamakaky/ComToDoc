#!/usr/bin/env python
# -*-coding:Utf-8 -*
import sys
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


rootDir = sys.argv[1]
listeFiles = getFiles(rootDir)
print(listeFiles)
