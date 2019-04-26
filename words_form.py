# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 19:37:15 2019

@author: Win
"""

from re import search, UNICODE
from pyaramorph import Analyzer
from pyaramorph.buckwalter import uni2buck

def get_forms(word):
    
    translit = uni2buck(word)
    w_forms = Analyzer().analyze_word(translit)
    
    forms = []
    for i in w_forms:
        forms.append(search(r'\((.+)\s(.+)\)',i,UNICODE).groups()[0])
    return (forms)
