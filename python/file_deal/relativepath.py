import os

p1='/home/suselslpp/Documents/python/file_deal/testcase_deal/funtion_two/function_one/sub_function/function_file2.txt'
p2='/home/suselslpp/Documents/python/file_deal/testcase_deal/function_one/sub_function/function_file.txt'
pb='/home/suselslpp/Documents/python/file_deal'
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
final=fatherdir+changetext