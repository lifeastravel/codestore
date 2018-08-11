import os
#get oldfilename
oldfilename=open("newfilename.txt",'r')
oldname_list=oldfilename.readlines()
oldfilename.close()
#get newfilename 
newfilename=open("oldfilename.txt",'r')
newname_list=newfilename.readlines()
newfilename.close()
#get name num
oldnamenum=len(oldname_list)
newnamenum=len(newname_list)

if oldnamenum != newnamenum:
  print "check your config file. make sure the old name eq the new name."
  exit()

print "*"*30+"the changing start"+'*'*30
for nameid in range(oldnamenum): 
    if os.path.isfile(oldname_list[nameid][:-1]):
        os.rename(oldname_list[nameid][:-1],newname_list[nameid][:-1])
        print "the "+str(nameid)+" file change ok"
    else:
        print "check the "+str(nameid)+" file, the file is not exiting."
    
print "*"*30+"the changing end"+'*'*30
print "="*30+"current dir including files"+"="*30
path=os.getcwd()
def VisitDir1(path):
 for root,dirs,files in os.walk(path):
   for filespath in files:
     print os.path.join(root,filespath)
VisitDir1(path)

print "="*80
