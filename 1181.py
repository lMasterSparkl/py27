#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john
#
# Created:     18/01/2018
# Copyright:   (c) john 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''c=[]
def prime(n):  #??2?n-1???????????
    global c
    for i in range(2,n):
        for j in range(2,i):
            if i%j==0 :
                break
            elif j==i-1:
                c.append(i)
    if a>=2:
        c=c.insert(0,2)
    c=c.reverse
    return c
def bi_search(x,y,z):
    if not(c in x):
        return -1
    else:
        mid=int((y+z)/2)
        if c==x[mid]:
            return mid
        elif c<x[mid]:
            z=mid
            return bi_search(x,0,z-1)
        else:
            y=mid
            return bi_search(x,y+1,z)
a=int(raw_input())
b=[]
b=prime(a)
lenb=len(b)-1
while True:
    c=int(raw_input())
    d=bi_search(b,0,lenb)
    print d  '''

def prime(n):
    c=[]
    for i in range(2,n):
        for j in range(2,i):
            if i%j==0 :
                break
            elif j==i-1:
                c.append(i)
    return c
def bi_search(x,y,z):
    if not(c in x):
        return -1
    else:
        mid=int((y+z)/2)
        if c==x[mid]:
            return mid
        elif c<x[mid]:
            z=mid
            return bi_search(x,0,z-1)
        else:
            y=mid
            return bi_search(x,y+1,z)
a=int(raw_input())
b=prime(a)
if a>=2:
    b.insert(0,2)
lenb=len(b)-1
c=int(raw_input())
d=bi_search(b,0,lenb)
print d

