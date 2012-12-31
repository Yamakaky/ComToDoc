#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Génère un fichier HTML à partir des objets Fonction"""

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import SubElement as sub_e


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

    
    tree = ET.ElementTree(racine)
    tree.write("doc.html")
