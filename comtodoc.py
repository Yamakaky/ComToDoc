#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from fonction import *
import comgetter
import htmlgen
import getopt
import os


output = "test.html"
version = "0.1"
name = "comToDoc"

def printUsage():
    print("help !")

def printVersion():
    global name
    global version
    print(name + " version " + version)
    
def parseArgs(args):
    try:
        opts, args = getopt.getopt(args, "ho:v", ["help", "output=", "version"])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(1)
    else:
        for o, a in opts:
            if o == "-h" or o == "--help":
                printUsage()
                sys.exit()
            elif o == "-o" or o == "--output":
                output = a
            elif o == "-v" or o == "--version":
                printVersion()
                sys.exit()

        if len(args) < 1:
            print("Il faut spécifier un nom de dossier")
            sys.exit(1)
        elif os.path.exists(args[0]):
            return args[0]
        else:
            print("Il faut spécifier un nom de dossier valable")
            sys.exit(1)

def main():
    # Gestion des arguments de la ligne de commande
    rootDir = parseArgs(sys.argv[1:])

    print("Création de la liste des fichiers...")
    listeFiles = comgetter.getFiles(rootDir)
    print("Lecture des fichiers...")
    commentaires = comgetter.getComs(listeFiles)
    print("Créaction des objets...")
    listeFonctions = Fonction.match(commentaires)

    print("Écriture du fichier...")
    global output
    if os.path.exists(output):
        os.remove(output)
    htmlgen.gen(listeFonctions, output)

    print("Fichier généré !")
    return 0

if __name__ == "__main__":
    sys.exit(main())
