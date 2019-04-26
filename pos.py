s=[[['و','wa', 'Par', 'P','p+'], ['ال','{l','par','DET', 'Al+'], ['تين','t~iyni', 'N','PN','M|GEN']]
   , [['و','wa','par','CONJ', 'CONJ+'], ['ال','{l','par','DET', 'Al+'], ['زيتون','z~ayotuwni', 'N','PN','|M|GEN']]
   , [['و','wa','par','CONJ', 'CONJ+'], ['طور','Tuwri', 'N','PN','|M|GEN']]
   , ['سينين','siyniyna','N','PN','GEN']
   , [['و','wa','Par','CONJ', 'CONJ+'], ['هذا','ha`*aA', 'PRON', 'DEM','MS']]
   , [['ال','{lo','Par','DET', 'Al+'], ['بلد','baladi', 'N', 'N' ,'M|GEN']]
   , [['ال','{lo', 'Par','DET', 'Al+'], ['أمين','>amiyni','N' ,'ADJ','|MS|GEN']]
   , [['ل','la','Par','EMPH', 'EMPH+'], ['قد','qado','PRON','CERT','']]
   , [['خلق','xalaqo', 'V', 'V|PERF','1P'], ['نا','naA', 'PRON', '','PRON:1P']]
   , [['ال','{lo', 'Par','DET', 'Al+'], ['أنسان','<insa`na', 'N','N' ,'M|ACC']]
   , ['في','fiY^', 'Par', 'P','']
   , ['أحسن','>aHosani', 'N','','|MS|GEN']
   , ['تقويم','taqowiymK', 'N', 'N|VN|(II)','M|INDEF|GEN']
   , ['ثم','vum~a','par', 'CONJ', '']
   , [['ردد','radado', 'V', 'V|PERF','1P'], ['نا','na`', 'PRON', '','1P'], ['ه','hu', 'PRON', 'PRON:3MS','']]
   , ['أسفل','>asofala', 'N', 'LOC','MS|ACC']
   , ['سافلين','sa`filiyna', 'N', 'N|ACT|PCPL','MP|GEN']
   , ['إلا','<il~aA','par','EXP', '']
   , ['اللذين','{l~a*iyna', 'PRON', 'REL','MP']
   , [['آمن',"'aAmanu", 'V', 'V|PERF|(IV)','3MP'], ['وا','wA@', 'PRON','', 'PRON:3MP']]
   , [['و','wa','par' ,'CONJ', 'w:CONJ+'], ['عمل','Eamilu', 'V', 'V|PERF|LEM','3MP'], ['وا','wA@', 'PRON', 'PRON:3MP','']]
   , [['ال','{l', 'par','DET', 'Al+'], ['صالحات','S~a`liHa`ti', 'N', 'N|ACT|PCPL','FP|ACC']]
   , [['ف','fa','par', 'REM', 'f:REM+'], ['ل','la','par' 'P', 'l:P+'], ['هم','humo', 'PRON', 'PRON|3MP','']]
   , ['أجر','>ajorN', 'N', 'VN','|M|INDEF|NOM']
   , ['غير','gayoru', 'N', '','M|NOM']
   , ['ممنون','mamonuwnK', 'N', 'N|PASS|PCPL','M|INDEF|GEN']
   , [['ف','fa', 'par''REM', 'f:REM+'], ['ما','maA','PRON' ,'INTG','']]
   , [['يكذب','yuka*~ibu', 'V', 'V|IMPF|(II)','3MS'], ['ك','ka', 'PRON', 'PRON:2MS','']]
   , ['بعد','baEodu','T' ,'T','']
   , [['ب','bi', 'par', 'P',''], ['ال','{l', 'par','DET', 'Al+'], ['دين','d~iyni', 'N', 'VN','|M|GEN']]
   , [['أ','>a','par' ,'INTG', 'INTG+'], ['ليس','layosa', 'V', 'V|PERF','SP:kaAn|3MS']]
   , ['الله','{ll~ahu', 'N','PN','NOM']
   , [['ب','bi', 'par','P', 'bi+'], ['أحكم','>aHokami', 'N', '','MS|GEN']]
   , [['ال','{lo','par','DET', 'Al+'], ['حاكمين','Ha`kimiyna', 'N', 'N|ACT|PCPL','MP|GEN']]]
s2=['والتين', 'والزيتون', 'وطور', 'سينين', 'وهذا', 'البلد', 'الأمين', 'لقد', 'خلقنا', 'الإنسان', 'في', 'أحسن', 'تقويم', 'ثم', 'رددناه', 'أسفل', 'سافلين', 'إلا', 'الذين', 'آمنوا', 'وعملوا', 'الصالحات', 'فلهم', 'أجر', 'غير', 'ممنون', 'فما', 'يكذبك', 'بعد', 'بالدين', 'أليس', 'الله', 'بأحكم', 'الحاكمين']
word=input('enterword: ')
c=0
def prints(list):
    print(list[0]+' , trancription is '+list[1]+' '+', pos is '+list[2]+' '+', sub catogery is '+' '+list[3]+' '+', feature is '+list[4])

for w in s2:
    
    if(w==word):
        i=c
    c=c+1
if(len(s[i])>4):
   prints(s[i])
else:
    for w in s[i]:
        prints(w)

