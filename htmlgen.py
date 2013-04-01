#!/usr/bin/env python

"""Génère un fichier HTML à partir des objets Fonction"""

import xml.etree.cElementTree as ET
from xml.etree.ElementTree import SubElement as sub_e
import os

def gen(liste_Fonction, file):
    """Prend en argument la liste des Fonction et génère le fichier html"""
    racine = ET.Element("html")

    
    head = sub_e(racine, "head")

    meta = sub_e(head, "meta")
    meta.set("charset", "utf-8")

    css = sub_e(head, "link")
    css.set("rel", "stylesheet")
    css.set("href", "style.css")
    css.set("type", "text/css")
    
    title = sub_e(head, "title")
    title.text = "Documentation"

    
    body = sub_e(racine, "body")

    
    h1 = sub_e(sub_e(body, "header"),
               "h1")
    h1.text = "Documentation"


    nav = sub_e(body, "nav")
    for f in liste_Fonction:
        li = sub_e(nav, "li")
        a = sub_e(li, "a")
        a.set("href", "#" + f.nom)
        a.text = f.nom


    section = sub_e(body, "section")

    for f in liste_Fonction:
        article = sub_e(section, "article")
        
        h = sub_e(article, "h1")
        h.text = f.nom

        p = sub_e(article, "p")
        p.text = f.description

        dl = sub_e(article, "dl")
        for key, value in f.args.items():
            dt = sub_e(dl, "dt")
            dt.text = key

            dd = sub_e(dl, "dd")
            dd.text = value
            
    indent(racine)
    
    tree = ET.ElementTree(racine)
    tree.write("tmp")
    with open("tmp") as tmp:
        with open(file, "w") as file:
            file.write("<!DOCTYPE html>\n")
            for line in tmp:
                file.write(line)
    os.remove("tmp")
    # J'ai pas réussit à faire plus propre
    
def indent(elem, level=0):
    """Fonction originale ici -> http://effbot.org/zone/element-lib.htm"""
    i = "\n" + level*"    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
