from re import *
from shutil import *
import os as o
from subprocess import *

d={}
valid_keys=open("valid_skus_in_shatha_folder.txt","r").readlines()

for i in valid_keys:
    s=search(r'\/(\d+)\_(\d+)(\.)',i)
    if s:
        if ( len(s.group(2)) < 4 ) and ( int(s.group(2)) > 10 ):
            d[s.group(1)]=1
    
for i in valid_keys:
    s1=search(r'\/(\d+)\_(\d+)(\.)',i)
    if s1:
        if s1.group(1) in d.keys():
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
            print(s1.group(2) + '->' + str(num) + '->' +  str(types) )
            


