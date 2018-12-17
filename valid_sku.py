from re import *
d={}
valid_keys=[]
invalid_keys=[]
sami=open("sami","r").readlines()
sami=[ i.strip() for i in sami ]
shatha=open("shatha","r").readlines()

for i in shatha:
    k=search(r'(?<=\/)\d+(?=\_)',i)
    if k:
        d[k.group()]=1

for i in sami:
    if i in d.keys():
        valid_keys.append(i)
    else:
        invalid_keys.append(i)

#print(len(valid_keys) + len(invalid_keys))

for i in invalid_keys:
    print(i)

