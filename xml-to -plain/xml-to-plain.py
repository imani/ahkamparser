# coding=utf8


from idlelib.IOBinding import encoding
import os
import codecs, sys, re
from pyquery import PyQuery as pq
from email.header import UTF8
from string import maketrans



path = 'D:\\ComputerEngineer\\Meshhkat\\Ahkam2\\'
dir = os.listdir(path+'second_edit\\')
file2q = open(path+'translation_edit\\'+'total_question.txt', 'w')
file2a = open(path+'translation_edit\\'+'total_answer.txt', 'w')
for filename in dir:
    print filename
    if filename[-4:] == '.xml':
        file = codecs.open(path+'second_edit\\'+filename, encoding='utf8').read()
        d = pq(file)
        qnum = 1
        anum = 1
        for q in d('question'):
            q = pq(q)
            qstring = q[0].text
            delimiters = u'.:!'.encode('utf8')
            for delim in delimiters:
                qstring = qstring.replace(delim,'')
            qstring = (qstring.replace('\n',' ').replace(delimiters[0],'') +'\n')
            file2q.write(qstring.encode('utf8'))
            qnum += 1
        for a in d('answer'):
            a = pq(a)
            astring = a[0].text
            astring = astring.replace('\n',' ')+'\n'
            file2a.write(astring.encode('utf8'))
            anum += 1 
        if qnum != anum:
            print 'q = '+ str(qnum) + ', a = '+ str(anum)       
file2q.close()
file2a.close()

print 'Finished!'
