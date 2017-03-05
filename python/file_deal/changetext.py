import os
import re
tempfile=open("testfile1.txt",'r+')
tempfilelist=tempfile.readlines()
i=0
for templine in tempfilelist:
  print templine
  print i
  matchstat=re.match("^test1\s+\w",templine)
  if matchstat:
    tempfilelist[i]="testjakl\n"
  i=i+1
tempfile=open("testfile1.txt",'w+')
tempfilelist=tempfile.writelines(tempfilelist)
tempfile.close()