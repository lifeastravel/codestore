import os
import re
def getfilenamepath(temppath):
  pathfileinclude=os.listdir(temppath)
  pathinclude=temppath
  localfilenamepath=[]
  for subpath in pathfileinclude:
    if os.path.isfile(pathinclude+"/"+subpath):
      tempfile=subpath
      temppath=pathinclude+"/"+subpath
      localfilenamepath.append([tempfile,temppath])
    elif os.path.isdir(pathinclude+"/"+subpath):
      temfilenamepath=getfilenamepath(pathinclude+"/"+subpath)
      localfilenamepath.extend(temfilenamepath) 
    else:
      localfilenamepath=[]
  return localfilenamepath

def changefiletext(filename,matchmode,changetext):
  tempfile=open(filename,'r+')
  tempfilelist=tempfile.readlines()
  i=0
  state=False
  tempfile.close()
  for templine in tempfilelist:
    matchstat=re.match(matchmode,templine)
    if matchstat:
      tempfilelist[i]=changetext+"\n"
      state=True
    i=i+1
  if state:
    tempfile=open(filename,'w+')
    tempfilelist=tempfile.writelines(tempfilelist)
    tempfile.close()
    
def getrelativepath(kpath,cpath,basepath)
  subsame=0
  fatherdir=''
  changetext=''
  p1path1,p1name1=os.path.split(p1)
  p1path2,p1name2=os.path.split(p2)
  path1=os.path.relpath(p1path1,pb)
  path2=os.path.relpath(p1path2,pb)
  path1list=path1.split('/')
  path2list=path2.split('/')
  len1=len(path1list)
  len2=len(path2list)
  if kpath==cpath:
    final=''
    return final
    break
  if len1<=len2:
    templen=len1
  else:
    templen=len2
  for i in range(templen):
    if path1list[i]==path2list[i]:
       subsame=subsame+1
    else:
      break
  for j in range(len2-subsame):
    fatherdir=fatherdir+'/'+'..'
  for k in range(subsame,len1):
    changetext=changetext+'/'+path1list[k]
  tempfinal=fatherdir+changetext
  final=tempfinal[1:]
  return final
  
  