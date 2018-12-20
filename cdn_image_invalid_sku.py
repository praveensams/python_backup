from re import *
import shutil as sh
from subprocess import *
x=0
d={
  'L_1': '01',
  'L_2':'02',
  'L_3': '03',
  'L_4': '04',
  'L_5': '05',
  'L_6': '06',
  'L_7': '07'
  }

s=open('invalid_sku_in_cdn_folder_list.txt','r').readlines()

for i in s:
    k=search(r'(?<=\/)(\d+)\_(\w\_[\w,\_]+)(.\w+)',i)
    if k:
        try:
            if search(r'L_[0-7]',k.group(2)):
                #print(k.group(1) + '_100_' + d[k.group(2)]  + k.group(3))
                k1=Popen('ls ' + i, stdout=PIPE,shell=True).communicate()[0].strip()
                sh.copy(k1,'/home/moniot/upload_cdn/' + k.group(1) + '_100_' + d[k.group(2)]  + k.group(3))
                print(k.group(1) + '_100_' + d[k.group(2)]  + k.group(3))
 
        except:
            pass

