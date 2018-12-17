from re import *
x=0
exclude=['00112192', '00163022', '00180636', '100008734', '100019934', '100019935', '100029078', '00189971', '00172173', '100019513', '100026540', '00189987']
shatha=open("shatha","r").readlines()
sami=open("sami","r").readlines()
skus={}

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
                skus[type.group(1)]=1
                if (len(type.group(2)) in (2,3) ) and ( type.group(1) not in exclude ):
                    pass
                else:
                    print(i)


print(len(skus.keys()))

