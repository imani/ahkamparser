'''
Created on Nov 12, 2012

@author: Hadi
'''

from lxml import etree
from lxml.builder import E
import os
import re
from xml.etree import ElementTree
from email.header import UTF8


if __name__ == '__main__':
    pass

path = 'D:\\ComputerEngineer\\Meshhkat\\Ahkam2\\'
dir = os.listdir(path)
file3 = open(path + 'categories.xml','w')
file3.write('<xml>\n')
for filename in dir:
    print filename
    if filename.__contains__('.htm'):
        file = open(path+'first_edit\\'+filename,'r')
        file2 = open(path+'second_edit\\'+filename[:-4]+'.xml', 'w')
        context = etree.iterparse(file)
        file2.write('<xml>')
        for action, elem in context:
            if (elem.tag == 'h3') & ('align' in elem.attrib.keys()):
            	cat = elem.text
                subcat = elem.text
                file3.write('<cat>'+cat.encode('utf-8'))
                file3.write('</cat>\n')
                
            elif elem.tag == 'h3':
                subcat = elem.text
                file3.write('\t<subcat cat=\"'+cat+'\">' + subcat.encode('utf-8') +'</subcat>\n')
            elif(elem.tag == 'p'):
                if (elem.attrib['style'] == 'font-weight: 600;font-size:11px;color:#303030'):
                    tag = 'question'                
                    match = re.search(r'-?\d+', elem.text)
                    id = int(match.group(0))
                    print id;
                    question = '<'+tag+' id=\"'+str(id)+'\" cat=\"'+cat+'\" subcat=\"'+subcat+'\">'                    
                    file2.write(question.encode('utf-8'))
                    file2.write(elem.text.encode('utf-8'))
                    file2.write('</question>')                    
                elif elem.attrib['style'] == 'margin-bottom: 12px':
                    tag = 'answer'
                    answer = '<'+tag+' id=\"'+str(id)+'\" cat=\"'+cat+'\" subcat=\"'+subcat+'\">'
                    file2.write(answer.encode('utf-8'))
                    file2.write(elem.text.encode('utf-8'))
                    file2.write('</answer>')
        file.close()
        file2.write('</xml>')
        file2.close()
file3.write('</xml>')
file3.close()
print 'Finished!'




 
