from re import *
from shutil import *
import os as o
from subprocess import *
x=0

d={}
valid_keys=open("valid_skus_in_shatha_folder_new.txt","r").readlines()

for i in valid_keys:
    s=search(r'\/(\d+)\_(\d+)(\.)',i)
    if s:
        if ( len(s.group(2)) < 4 ) and ( int(s.group(2)) > 10 ):
            d[s.group(1)]=1
    
for i in valid_keys:
    s1=search(r'\/(\d+)\_(\d+)(\.)(\w+)',i)
    if s1:
        if s1.group(1) in d.keys():
            print("Matching lists -->  " + s1.group(1))
            pass
        else:
            if len(s1.group(2)) > 3:
                if int(s1.group(2)) < 10:
                    num="0{}".format(int(s1.group(2)))
                    types=200
                else:
                    num=int(s1.group(2))
                    types=200
            else:
                if int(s1.group(2)) < 10:
                    num="0{}".format(int(s1.group(2)))
                    types=100
                else:
                    num=int(s1.group(2))
                    types=100
            copy('/python/' + i.strip(),'/upload/valid_sku_shatha_folder/' + str(s1.group(1)) + '_' +  str(types) + '_' + str(num) + '.' + str(s1.group(4)) ) 
            x+=1
            print("Total remaining to convert: {}".format(39227 - x))


