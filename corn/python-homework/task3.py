import sys
import math

#print('kvadratniy koren chisla ' + sys.argv[1] + ' eto', math.sqrt(int(sys.argv[1])))
print('kvadratniy koren chisla {chislo} eto {answer}'.format(chislo = sys.argv[1], answer = math.sqrt(int(sys.argv[1] ))))
