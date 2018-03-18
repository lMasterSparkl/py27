#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john
#
# Created:     14/01/2018
# Copyright:   (c) john 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''num=int(raw_input())
sum=0
for i in range(num):
    if i%3==0 or i%5==0:
        sum+=i
print sum '''
import math
num=int(raw_input())
zongshu=0
for i in range(2,num):
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j==0 :
            break
    else:
        a=i
        stra=str(a)
        count=len(stra)
        isnumber=0
        notnumber=0
        for b in range (1,count):
            strnew=stra[count-1]+stra[0:count-1]

            intstr=int(strnew)
            for c in range(2,int(math.sqrt(intstr)+1)):

                if intstr%c==0:
                    notnumber+=1
                    break
            else:
                isnumber+=1
            stra=strnew
        else:

            if notnumber==0 and isnumber==count-1:
                zongshu+=1
print zongshu
'''a=12345
stra=str(a)
count=len(stra)
b=stra[count-1]+stra[0:count-1]
print a
print stra
print count
print b'''
























