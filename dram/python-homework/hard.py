import sys

#print('<ul>')
#print('<li>')

#for param in sys.argv[1:]:
#    print (param)
#print('</li>')
#print('<li>')
#for param in sys.argv[1:]:
#    print (param.upper())
#print('</li>')
#print('<li>')
#for param in sys.argv[1:]:
#    print (param.lower())
#print('</li>')
#print('</ul>')
str_input = ""
for param in sys.argv[1:]:
    str_input += param + " "
my_html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>List</title>
  </head>
  <body>
    <ul>
        <li>{orig}</li>
        <li>{lower}</li>
        <li>{upper}</li>
    </ul>
  </body>
</html>""".format(orig = str_input, lower = str_input.lower(), upper = str_input.upper())

print(my_html)
