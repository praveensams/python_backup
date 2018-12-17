from re import *
x=0
exclude={}
shatha=open("shatha","r").readlines()
sami=open("sami","r").readlines()

sami_list=[]
shatha_list=[]

for i in sami:
    l=i.rstrip()
    sami_list.append(l)

for i in shatha:
    i=i.strip()
    sku=search(r'(?<=\/)\d+(?=\_)',i)
    if sku:
        if sku.group() in sami_list:
            type=search(r'\/(\d+)\_(\d+)\.jpg',i)
	    if type:
                if (len(type.group(2)) in (2,3) ):
	            if int(type.group(2)) > 11:
                        exclude[type.group(1)]=1
                        pass
                    else:
                        print(i)


print(exclude.keys())
