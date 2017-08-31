# -*- coding: UTF-8 -*-

import time
import sys
import os

curDir = sys.path[0]

f = open('text.lua','r')
content = []
for data in f.readlines():
	content.append(data)

f.close()
print content
curFile = curDir + '/res.txt'
f1 = open(curFile,'w')
f1.write('\"')
for data in content:
	s = data.rstrip('\n')
	s = s.replace('\"','\'')
	f1.write(s + '\\n')
f1.write('\"')
f1.close()

