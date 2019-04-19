#!/usr/bin/env python
# coding: utf-8

from light_stemmer import light_stemmer
from root_based_stemmer import get_root

text="المدرسة المدينة المديرة يفعلون تفعلان تكتبين نكتب"

def stemmer(text):
    stems = light_stemmer(text)
    for s in stems:
        print(s)
        print (get_root(s[1]),'\n\n#####\n')


stemmer(text)
