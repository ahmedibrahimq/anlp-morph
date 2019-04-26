#!/usr/bin/env python
# coding: utf-8

from re import search, UNICODE
from pyaramorph import Analyzer
from pyaramorph.buckwalter import uni2buck

def get_forms(word='فعل'):
    
    translit = uni2buck(word)
    w_forms = Analyzer().analyze_word(translit)
    
    forms = []
    for i in w_forms:
        forms.append(search(r'\((.+)\s(.+)\)',i,UNICODE).groups())
    return (word,forms)

    
