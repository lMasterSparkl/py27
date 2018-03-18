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
'''
int Cre(int n,int k):
{
    if (n==k)
    {
        return 1;
    }
    if (k==0)
    {
        return 1;
    }
    if (k==1)
    {
        return n;
    }
    if (n==1)
    {
        return 1;
    }
    return Cre(n-1,k-1)+Cre(n-1,k);
} '''
a = []
k = int(raw_input())
for i in range(k):
    a.append([' '])
    for j in range(k):
        a[i].append(0)

for i in range(k):
    a[i][0] = 1
    a[i][i] = 1

for i in range(2,k):
    for j in range(1,i):
        a[i][j] = a[i - 1][j-1] + a[i - 1][j]

from sys import stdout

for i in range(k):
    for j in range(i + 1):
        stdout.write(a[i][j])
        stdout.write(' ')
    print

