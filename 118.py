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
import random


num = ['2','3','4','5']

fuhao = ['-','+','/','*','**']

stringnew = ''



while stringnew != 28:

   r = random.sample(fuhao,3)

   n = random.sample(num,4)

#print r,'ok',r[0],r[1],r[2]

#print n,'ok',n[0],n[1],n[2],n[3]

   new = n[0]+ r[0]+n[1]+ r[1]+n[2]+ r[2]+n[3]

   stringnew = eval(new)

print new,eval(new)