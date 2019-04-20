#!/usr/bin/env python
# coding: utf-8

from light_stemmer import light_stemmer
from QuarnicArabicCorpus.roots import roots

wzn = [[3, [0, 1, 2], '', 'فعل'], [4, [0, 1, 2], 'ل', 'فعلل'], [5, [1, 3, 4], 'ات', 'افتعل'], [4, [0, 2, 3], 'ا', 'فاعل'], [5, [2, 3, 4], 'ان', 'انفعل'], [6, [3, 4, 5], 'است', 'استفعل'], [5, [1, 3, 4], 'مت', 'مفتعل'], [5, [1, 2, 4], 'مو', 'مفعول'], [4, [0, 1, 3], 'ا', 'فعال'], [4, [0, 1, 3], 'و', 'فعول'], [4, [0, 1, 3], 'ي', 'فعيل'], [5, [1, 2, 4], 'ما', 'مفعال'], [5, [1, 2, 4], 'مي', 'مفعيل'], [4, [0, 1, 2], 'ة', 'فعلة'], [5, [0, 1, 2], 'يل', 'فعليل'], [4, [1, 2, 3], 'أ', 'أفعل'], [4, [1, 2, 3], 'ا', 'افعل'], [5, [0, 1, 2], 'اء', 'فعلاء'], [5, [0, 1, 2], 'ان', 'فعلان'], [4, [0, 1, 2], 'ى', 'فعلى'], [4, [0, 2, 3], 'ي', 'فيعل'], [4, [1, 2, 3], 'م', 'مفعل'], [5, [1, 2, 3], 'مة', 'مفعلة'], [5, [0, 1, 3], 'اة', 'فعالة'], [5, [0, 2, 3], 'اة', 'فاعلة'], [5, [0, 2, 4], 'او', 'فاعول'], [5, [1, 3, 4], 'تا', 'تفاعل'], [7, [3, 4, 6], 'استا', 'استفعال'], [4, [1, 2, 3], 'ت', 'تفعل'], [4, [0, 2, 3], 'و', 'فوعل'], [5, [0, 1, 3], 'يل', 'فعيلل'], [4, [0, 1, 2], 'ي', 'فعلي'], [3, [0, 2, 1], '', 'فلع'], [3, [1, 0, 2], '', 'عفل'], [4, [3, 0, 2], 'ا', 'عالف'], [5, [0, 1, 4], 'ائ', 'فعائل'], [4, [0, 2, 3], 'و', 'فوعل'], [5, [0, 3, 4], 'وا', 'فواعل']]
text="المدرسة المدينة المديرة يفعلون تفعلان تكتبين نكتب"

def remove_root(stem, root_pos):
    root =[ stem[root_pos[0]], stem[root_pos[1]], stem[root_pos[2]] ]
    root_removed = stem[:root_pos[0]] + stem[root_pos[0]+1 : root_pos[1]] + stem[root_pos[1]+1 : root_pos[2]] + stem[root_pos[2]+1:]
    return (root_removed,root)

def check_root(r):
    if r in roots:
        return True
    return False


def get_root(stem):
    stem_len= len(stem)
    roots=[]
    for w in wzn:
        if w[0]==stem_len:
            root_pos=w[1]
            root_removed, root = remove_root(stem,root_pos)
            if w[2]==root_removed:
                roots.append((root, w[3], check_root(''.join(root))))
    return roots


def stemmer(text):
    stems = light_stemmer(text)
    for s in stems:
        print(s)
        print (get_root(s[1]),'\n\n#####\n')


stemmer(text)
