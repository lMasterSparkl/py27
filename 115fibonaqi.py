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
'''
1?????

??????????10???1, 2, 3, 5, 8, 13, 21, 34, 55, 89?????????????n??????????????????

????:

?????n??100?
?????
?????????? 2 + 8 + 34 = 44?
?????
100
?????
44
?????500ms
??????
numb=int(raw_input())
count=0
def fibonaqi(n):
    if n==0 or n==1:
        return n
    else:
        return fibonaqi(n-1)+fibonaqi(n-2)
for i in range(2,numb):
    a=fibonaqi(i)
    if a<numb and a%2==0:
        count+=a
    elif a>numb:
        break
print count

??????
num=int(raw_input())
n=1
a=0
b=1
count=0
while n :
    c=a+b
    if c<num and c%2==0:
        count+=c
        a=b
        b=c
    elif c>num:
        break
    else:
        a=b
        b=c
print count  '''












