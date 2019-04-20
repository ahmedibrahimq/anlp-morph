#!/usr/bin/env python
# coding: utf-8

from nltk import CFG
from nltk.parse import RecursiveDescentParser
from nltk.parse import ShiftReduceParser
from nltk.parse import LeftCornerChartParser
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NS|VS
NS -> SBJ PRD
VS -> V0 SBJ | V1 SBJ OBJ1 | V2 SBJ OBJ1 OBJ2
PRD -> N|PP|NS|VS
PP -> P N
SBJ -> N
OBJ1 -> N
OBJ2 -> N
N -> 'الماء'|'الكريم'|'الكثير'|'الشجاع'|'الرسول'|'محمد'|'الطفل'|'العدو'|'الصاحب'|'الطالب'|'الدرس'|'الصلاة'|'الحق'|'المسافر'|'الطريق'|'الرجل'|'الخطأ'|'الأرض'|'كل'|'ثوب'|'جديد'|'درس'|'سهل'|'ماء'|'كريم'|'كثير'|'شجاع'|'رسول'|'طفل'|'عدو'|'صاحب'|'طالب'|'صلاة'|'حق'|'مسافر'|'طريق'|'رجل'|'خطأ'|'أرض'|'صاحبه'|'حقه'|'الامتحان'
P -> 'في'|'الى'|'من'|'عن'|'على'
V0 -> 'تفتح'|'فاض'|'ثار'|'هبت'|'جلس'|'ضاع'|'خرج'|'نام'|'وقعد'|'سافر'|'صدق'|'زرع'
V1 -> 'طوى'|'أكل'|'بلل'|'زرع'|'أطفأ'|'يركب'|'يستجيب'|'حفظ'|'كتب'|'شاهد'|'قال'
V2 -> 'يسقي'|'كسا'|'أعطى'|'ظن'|'حسب'|'جعل'|'خال'|'منح'|'منع'|'ألبس'
""")

grammar_reduced = CFG.fromstring("""
S -> NS|VS
NS -> N N
VS -> V0 N | V1 N N | V2 N N N
PP -> P N
N -> 'الماء'|'الكريم'|'الكثير'|'الشجاع'|'الرسول'|'محمد'|'الطفل'|'العدو'|'الصاحب'|'الطالب'|'الدرس'|'الصلاة'|'الحق'|'المسافر'|'الطريق'|'الرجل'|'الخطأ'|'الأرض'|'كل'|'ثوب'|'جديد'|'درس'|'سهل'|'ماء'|'كريم'|'كثير'|'شجاع'|'رسول'|'طفل'|'عدو'|'صاحب'|'طالب'|'صلاة'|'حق'|'مسافر'|'طريق'|'رجل'|'خطأ'|'أرض'|'صاحبه'|'حقه'|'الامتحان'
P -> 'في'|'الى'|'من'|'عن'|'على'
V0 -> 'تفتح'|'فاض'|'ثار'|'هبت'|'جلس'|'ضاع'|'خرج'|'نام'|'وقعد'|'سافر'|'صدق'
V1 -> 'طوى'|'أكل'|'بلل'|'زرع'|'أطفأ'|'يركب'|'يستجيب'|'حفظ'|'كتب'|'شاهد'|'قال'
V2 -> 'يسقي'|'كسا'|'أعطى'|'ظن'|'حسب'|'جعل'|'خال'|'منح'|'منع'|'ألبس'
""")

#####RecursiveDescentParser######

tdParser = RecursiveDescentParser(grammar)
def rdp(s):
    for w in tdParser.parse(s.split()):
        print (w)

#####ShiftReduceParser#####

srPraser = ShiftReduceParser(grammar_reduced,2)
def srp(s):
    for w in srPraser.parse(s.split()):
        print (w)

#####LeftCornerParser#####

lcPraser = LeftCornerChartParser(grammar)
def lcp(s):
    for w in lcPraser.parse(s.split()):
        print (w)

#####EarleyParser#####

ePraser = EarleyChartParser(grammar)
def ep(s):
    for w in ePraser.parse(s.split()):
        print (w)
