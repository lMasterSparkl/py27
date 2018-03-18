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

a=[1,3,5,7,8,10,12]
b=[4,6,9,11]
c=[2]
y=0
count=0
d=365
for i in range(0,100):
    y=1901+i

    for k in range(1,13):
        if k in a:
            if d%7==6:
                count+=1
            d=d+31
        elif (k in c)and(y%4==0 and y%100!=0 or y%400==0):
            if d%7==6:
                count+=1
            d=d+29
        elif (k in c)and(not(y%4==0 and y%100!=0 or y%400==0)):
            if  d %7==6:
                count+=1
            d=d+28
        else:
            if d %7==6:
                count+=1
            d=d+30
print count






