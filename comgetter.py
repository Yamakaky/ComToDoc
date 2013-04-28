#!/usr/bin/env python

import os.path
import re
import glob

re_dasm = re.compile(r'.dasm$')
re_com = re.compile(r'^(;;; *)')

def get_files(dir_name):
    """ Liste <dir> et renvoie la liste des .dasm qu'il contient (récursif) """
    
    for file_name in glob.glob(dir_name + "/*"):
        if os.path.isdir(file_name):
            for sub_file in get_files(file_name):
                yield sub_file
        elif re_dasm.match(file_name):
            yield file_name


def get_coms(file_name):
    """ Retourne la liste des lignes utilisées pour la doc """
    for line in open(file_name, "r").read().splitlines():
        if re_com.match(line): 
            yield re_com.sub('', line)
