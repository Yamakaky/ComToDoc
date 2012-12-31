#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from fonction import *
from comGetter import *


def printHelp():
    print("help !")

def main():
    if len(sys.argv) < 2:
        print("argument manquant")
        return 1

    arg = sys.argv[1]

    if arg == "--help" or arg == "-h":
        printHelp()
        return 0
    elif not os.path.exists(arg):
        print("Dossier en argument introuvable")
        return 1


    rootDir = sys.argv[1]
    print("Création de la liste des fichiers...")
    listeFiles = getFiles(rootDir)
    print("Lecture des fichiers...")
    commentaires = getComs(listeFiles)
    print("Créaction des objets...")
    listeFonctions = Fonction.match(commentaires)

    print("Écriture du fichier...")
    if os.path.exists("test.html"):
        os.remove("test.html")

    with open("test.html", "a") as file:
        html = "<!DOCTYPE HTML>"
        html += """<html>
                   <head>
                     <meta charset=\"utf-8\" />
                     <title>Documentation de FrOSt</title>
                   </head>
                   <body>"""
        for fonction in listeFonctions:
            html += fonction.getHTML()

        html += "</body></html>"
        file.write(html)

    print("Fichier généré !")
    return 0


if __name__ == "__main__":
    sys.exit(main())
