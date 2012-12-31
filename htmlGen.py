#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Génère un fichier HTML à partir des objets Fonction"""

import xml.etree.cElementTree as ET
from xml.etree.ElementTree import SubElement as sub_e
import os


def gen(liste_Fonction):
    """Prend en argument la liste des Fonction et génère le fichier html"""
    racine = ET.Element("html")

    
    head = sub_e(racine, "head")

    meta = sub_e(head, "meta")
    meta.set("charset", "utf-8")

    css = sub_e(head, "link")
    css.set("rel", "stylesheet")
    css.set("href", "style.css")
    
    title = sub_e(head, "title")
    title.text = "Une super documentation !"

    
    body = sub_e(racine, "body")

    for f in liste_Fonction:
        section = sub_e(body, "section")
        
        h = sub_e(section, "h1")
        h.text = f.m_nom

        p = sub_e(section, "p")
        p.text = f.m_description

        dl = sub_e(section, "dl")
        for key, value in f.m_args.items():
            dt = sub_e(dl, "dt")
            dt.text = key

            dd = sub_e(dl, "dd")
            dd.text = value
            
    indent(racine)
    
    tree = ET.ElementTree(racine)
    tree.write("tmp")
    with open("tmp") as tmp:
        with open("doc.html", "w") as file:
            file.write("<!DOCTYPE html>\n")
            for line in tmp:
                file.write(line)
    os.remove("tmp")
    # J'ai pas réussit à faire plus propre

    
def indent(elem, level=0):
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
