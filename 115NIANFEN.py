#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john
#
# Created:     15/01/2018
# Copyright:   (c) john 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
aa=int(raw_input())
bb=int(raw_input())
yy=aa-1800
a=[1,3,5,7,8,10,12]
b=[4,6,9,11]
c=[2]
y=0
d=0
for i in range(0,yy):
    y=1800+i
    if y%4==0 and y%100!=0 or y%400==0:
        d=d+366
    else:
        d+=365
y+=1
for k in range(1,bb+1):

    if k in a:
        d=d+31
    elif (k in c)and(y%4==0 and y%100!=0 or y%400==0):
        d=d+29
    elif (k in c)and(not(y%4==0 and y%100!=0 or y%400==0)):
        d=d+28
    else:
        d=d+30
e=(d+2)%7
print e