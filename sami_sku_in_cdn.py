invalid_keys=open('invalid_keys','r').readlines()
cdn_keys=open('cdn_product','r').readlines()
k=[]
x=0

invalid_keys=[ i.strip() for i in invalid_keys ]
cdn_keys=[ i.strip() for i in cdn_keys ]

for i in invalid_keys:
    if i in cdn_keys:
        x+=1   

print(x)
