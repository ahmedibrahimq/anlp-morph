from nltk.corpus import wordnet as wn
def wordnets(word,lang1,lang2):
    w=wn.synsets(word,lang=lang1)
    myset=set()
    myset2=set()
    for s in w:
        for l in s.lemmas(lang=lang2):
            myset.add(l.name())
            for n in l.antonyms():
                myset2.add(n.name())
    return(myset,myset2)
