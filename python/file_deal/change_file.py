 
from getfilepath import getfilenamepath,changefiletext

import os
localfilenamepath=[]
currentpath=os.getcwd()
changefilepath=currentpath+"/testcase_deal"
filepath1=getfilenamepath(changefilepath)
filepath2=getfilenamepath(changefilepath)

i=0

print filepath1

for temp in filepath1:
  if i==3:
    break
  name=temp[0]
  needchangepath=temp[1]
  print "=========================start "+str(i)+"============="
  print name
  print needchangepath
  print "=========================end==============="
  i=i+1
  #changefiletext(str(needchangepath),"^this\s+\w","thiss a test")

