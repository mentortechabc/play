import sys

#print('<ul>\n\t  <li> Original text:\n\t\t <ul>\n\t\t\t <li>' + sys.argv[1] + '\n\t\t</ul>\n\t',
#                '<li> All letters big:\n\t\t <ul>\n\t\t\t <li>' + sys.argv[1].upper()+'\n\t\t</ul>\n\t',
 #               '<li> All letters small:\n\t\t <ul>\n\t\t\t <li>' + sys.argv[1].lower()+'\n\t\t</ul>\n</ul>')

# Вариант через .format
html = (""" 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
    <body>
    <ul>
         <li> Original text: </li>
             <ul>
                 <li> {original}</li>
             </ul>
         <li> All letters big:</li>
             <ul>
                 <li> {upper} </li>
             </ul>
        <li> All letters small:</li>
             <ul>
                 <li> {lower} </li>
             </ul>
    </ul>
    </body>
</html>
    """.format(original = sys.argv[1],upper = sys.argv[1].upper(),lower = sys.argv[1].lower()))
    
    
print(html)
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
