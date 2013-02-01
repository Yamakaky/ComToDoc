#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from fonction import Fonction
import comgetter
import htmlgen
import getopt
import os


output = "doc.html"
version = "0.1"
name = "comToDoc"

def print_usage():
    print("help !")

def print_version():
    global name
    global version
    print(name + " version " + version)
    
def parse_args(args):
    try:
        opts, args = getopt.getopt(args, "ho:v", ["help", "output=", "version"])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(1)
    else:
        for o, a in opts:
            if o == "-h" or o == "--help":
                print_usage()
                sys.exit()
            elif o == "-o" or o == "--output":
                global output
                output = a
            elif o == "-v" or o == "--version":
                print_version()
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
    root_dir = parse_args(sys.argv[1:])

    print("Création de la liste des fichiers...")
    liste_files = comgetter.get_files(root_dir)
    print("Lecture des fichiers...")
    commentaires = comgetter.get_coms(liste_files)
    print("Créaction des objets...")
    liste_fonctions = Fonction.match(commentaires)

    print("Écriture du fichier...")
    global output
    if os.path.exists(output):
        os.remove(output)
    htmlgen.gen(liste_fonctions, output)

    print("Fichier généré !")
    return 0

if __name__ == "__main__":
    sys.exit(main())
