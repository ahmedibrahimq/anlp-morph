# Arabic Morphological Analyzer

### Main components

* ### Root Based Stemmer
Applied after removing affixes and clitics from the word, with the light stemmer we built, based on [Tashaphyne afixes list](https://github.com/linuxscout/tashaphyne/blob/master/tashaphyne/stem_const.py). Then, we compare the stem with patterns -(الميزان الصرفي), which have the same length of the stem. This is done by removing -from the stem, chracters which corresponding to the root radicals of the pattern, and matching  the remaining with each pattern after removing root radical from it. Last step is verifing the matched root(s) for the stem with a dictionary of roots extracted from [Quranic Arabic Corpus](http://corpus.quran.com/). 

* ### POS Tagger and Morphological features
Applied on  sūrat l-tīn, based on [QADT](http://corpus.quran.com/documentation/grammar.jsp).

* ### Synonyms and Antonyms
@elkharashy22 developed a wider searching technique in [wordnet](https://wordnet.princeton.edu/) for antonomys written in arabic script.

In collaboration with @elkharashy22
