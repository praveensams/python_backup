from re import *
shatha=open("shatha","r").readlines()
sami=open("sami","r").readlines()
sami=[ i.strip() for i in sami ]
list={}

for i in shatha:
    sku=search(r'(?<=\/)\d+(?=\_)',i)
    if sku:
        if sku.group() in sami:
            list[sku.group()]=1 

for i in (list.keys()):
    print(i)
