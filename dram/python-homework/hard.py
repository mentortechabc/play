import sys

print('<ul>')
print('<li>')
if __name__ == "__main__":
    for param in sys.argv[1:]:
        print (param)
print('</li>')
print('<li>')
if __name__ == "__main__":
        for param in sys.argv[1:]:
            print (param.upper())
print('</li>')
print('<li>')
if __name__ == "__main__":
    for param in sys.argv[1:]:
        print (param.lower())
print('</li>')
print('</ul>')
