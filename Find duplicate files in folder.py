#find the duplicate files by name.
#provide the folder name in which you want to find the duplicatess
import os

fnap = []
from os.path import join, getsize
for root, dirs, files in os.walk('K:\\Photos'):
    for f in files:
        fnap.append([f,root])
fnap.sort(key = lambda x:x[0])
dup = []
count = 1
for i in range(1,len(fnap)):
    if fnap[i-1][0] == fnap[i][0]:
        count+=1
    else:
        if count>1:
            duppath = []
            for t in range(1,count+1):
                duppath.append(fnap[i-t][1])
            dup.append([fnap[i-1][0],count,duppath])
        count=1
if count>1:
    dup.append([fnap[i-1][0],count])
    count=0
total = 0
for t in dup:
    #print(t)
    total+=t[1]-1
for t in dup:
    print(t[0],t[1])
    for path in t[2]:
        print(path)
    print('')

print('total duplicates ',total)
