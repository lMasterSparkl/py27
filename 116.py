#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john
#
# Created:     16/01/2018
# Copyright:   (c) john 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
stra=str(raw_input())
stra=stra.lower()
stra1=stra.split(' ')
for i in range(len(stra1)):
    a=stra1[i]
    if a[0] in 'aeiou':
        stra1[i]=a+'hay'
    elif a[:2]=='qu':
        stra1[i]=a[2:]+'quay'
    else:
        for j in range(1,len(a)):
            if a[j] in 'aeiouy':
                stra1[i]=a[j:]+a[:j]+'ay'
                break
    print stra1[i],


'''elif a[0]=='q' and a.find('u'):
        b=a.find('u')
        count=count +' '+a[1:b]+a[b+1:]+'quay'

        elif a[:2]=='qu':
        count=count+' ' +a[2:]+'quay'

        '''
