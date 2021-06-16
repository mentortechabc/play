import sys

print('<ul>\n\t  <li> Original text:\n\t\t <ul>\n\t\t\t <li>' + sys.argv[1] + '\n\t\t</ul>\n\t',
                '<li> All letters big:\n\t\t <ul>\n\t\t\t <li>' + sys.argv[1].upper()+'\n\t\t</ul>\n\t',
                '<li> All letters small:\n\t\t <ul>\n\t\t\t <li>' + sys.argv[1].lower()+'\n\t\t</ul>\n</ul>')

# Вариант через .format
#print('<ul>\n\t <li> Original text:\n\t\t <ul>\n\t\t\t <li> {}\n\t\t </ul>\n\t <li> All letters big:\n\t\t <ul>\n\t\t\t <li> {} \n\t\t </ul>\n\t <li> All letters small:\n\t\t <ul>\n\t\t\t <li> {} \n\t\t </ul>\n </ul>'.format(sys.argv[1],sys.argv[1].upper(),sys.argv[1].lower()))

#более читабельный для человека
'''
print('<ul>\n\t'
        '<li>Original text:\n\t\t'
             '<ul>\n\t\t\t'  
                 '<li>' + sys.argv[1]+'\n\t\t'
             '</ul>\n\t',
        '<li>All letters big:\n\t\t'
             '<ul>\n\t\t\t'  
                 '<li>' + sys.argv[1].upper()+'\n\t\t'
             '</ul>\n\t',
        '<li>All letters small:\n\t\t'
                '<ul>\n\t\t\t'  
                    '<li>' + sys.argv[1].lower()+'\n\t\t'
                '</ul>\n'
       '</ul>')
'''