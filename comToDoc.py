#!/usr/bin/env python
# -*-coding:Utf-8 -*
import sys
from comGetter import *


def printHelp():
    print("help !")


if len(sys.argv) < 2:
    print("argument manquant")
    sys.exit(1)

arg = sys.argv[1]

if arg == "--help" or arg == "-h":
    printHelp()
    sys.exit(0)
elif not os.path.exists(arg):
    print("Dossier en argument introuvable")
    sys.exit(1)
    

rootDir = sys.argv[1]
listeFiles = getFiles(rootDir)
commentaires = getComs(listeFiles)
print(commentaires)
for line in commentaires:
    print(line)
