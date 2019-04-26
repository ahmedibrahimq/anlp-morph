# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:54:10 2019

@author: Win
"""
from word_net import wordnets
from words_form import get_forms
list=get_forms("خير")
print(list) 
def syn_ant_get(word):
    synset,antset=wordnets(word,"arb","arb")
    synset1,antset=wordnets(word,'arb','eng')
    synset2=set()
    if(len(antset)!=0):
        synset2,antset=wordnets(antset.pop(),'eng','arb')
        
    return (synset,synset2)
for w in list:
    synset,antset=syn_ant_get(w)
    if(len(synset)!=0):
        print("synonyms of "+w,synset)
    if(len(antset)!=0):    
        print("antonyms of "+w,antset)
    