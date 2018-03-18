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
def hanoi(n,X,Y,Z):
    if n == 0:
        return
    else:
        hanoi(n - 1, X, Z, Y)
        print 'Move', n, 'from', X, 'to', Z
        hanoi(n - 1, Y, X, Z)
num=int(raw_input())
hanoi(num,'A','B','C')