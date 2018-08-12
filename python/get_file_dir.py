import os
print "="*80

def VisitDir(arg,dirname,names):
  for filespath in names:
    print os.path.join(dirname,filespath)
#get current directory.
path=os.getcwd()
#get current directory inclued file and directory(sub dir and sub file).
os.path.walk(path,VisitDir,())

print "="*80

def VisitDir1(path):
  for root,dirs,files in os.walk(path):
    print root
    print dirs
    print files
    print '*'*80
    for filespath in files:
      print os.path.join(root,filespath)
      print '-'*80
#get current directory include file(subdir include file)
VisitDir1(path)

print "="*80
#get currentdir inclued file and dir.
os.listdir('.')
