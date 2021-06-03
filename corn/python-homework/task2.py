import sys

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

