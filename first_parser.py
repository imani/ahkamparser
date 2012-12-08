'''
Created on Nov 7, 2012

@author: Hadi
'''
from Canvas import Line
from lxml import etree
import os
import re

if __name__ == '__main__':
    pass

path = 'D:\\ComputerEngineer\\Meshhkat\\Ahkam2\\'
dir = os.listdir(path)
for filename in dir:
    print filename
    if filename.__contains__('.htm'):
        file = open(path+filename,'r')
        file2 = open(path+'first_edit\\'+filename, 'w')
        tree = etree.parse(file, etree.HTMLParser())
        for core in tree.xpath('//div[@id="Secton_Box_Container"]'):
            s = unicode.encode(etree.tounicode(core))
            s = re.sub('<br/>', '\n', s)
            file2.write(s)
        file.close()
        file2.close()
print 'Finished!'

