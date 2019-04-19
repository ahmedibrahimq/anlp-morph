#!/usr/bin/env python
# coding: utf-8

from Tashaphyne import affixes


prefixes=affixes.prefixes()
suffixes=affixes.suffixes()


def Tokenize(text):
    tokens=text.split()
    return tokens


def get_prefix(token):
    prefix = ''
    for p in prefixes:
        if token.startswith(p):
            prefix = p
    return prefix


def get_suffix(token):
    suffix = ''
    for s in suffixes:
        if token.endswith(s):
            suffix = s
    return suffix


def get_stem(token, prefix_len, suffix_len):
    return token[prefix_len : len(token) - suffix_len]


def light_stemmer(text):
    prefix=""
    suffix=""
    stem=""

    tokens=Tokenize(text)
    stems = []
    
    for t in tokens:
        prefix = get_prefix(t)
        suffix = get_suffix(t)
        stem = get_stem(t, len(prefix), len(suffix))

        #print (" prefix: "+prefix+" stem: "+stem+" suffix: "+suffix)
        stems.append([prefix, stem, suffix])
        prefix=""
        suffix=""
    return stems
