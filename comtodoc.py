#!/usr/bin/env python

import sys
import os
import argparse

from fonction import Fonction
import comgetter
import htmlgen

output = "doc.html"
version = "0.1"
name = "comToDoc"

def print_version():
    """Affiche le nom et la version du soft."""
    global name
    global version
    print(name + " version " + version)
    sys.exit(0)
    
def parse_args(args):
    """Parse et gère les arguments en ligne de commande.
    Argument :
    -- args : liste des arguments passés au programme (typiquement : sys.argv(1:))

    Retour :
    -- args[0], le fichier/dossier contenant les sources dasm.
    """
    global output

    parser = argparse.ArgumentParser(description="Génère un doc HTML à partir d'un programme en DASM")
    
    parser.add_argument("-o", "--output", dest="output", help="La documentation sera écrite dans FILE", metavar="FILE")
    parser.add_argument("-v", "--version", action="store_true", dest="bool_print_version", default=False, help="Affiche la version du soft")
    parser.add_argument("dir", nargs=1, metavar="DIR", help="Le dossier contenant les sources DASM")
    
    args = vars(parser.parse_args())

    for key, value in args:
        if key == bool_print_version and value is True:
            print_version()

    return args[dir]
    
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
