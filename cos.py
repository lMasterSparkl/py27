#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john
#
# Created:     13/01/2018
# Copyright:   (c) john 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
a=float(raw_input())
b=float(raw_input())
c=float(raw_input())
d=(a*a+b*b-c*c)/(2*a*b)
e=math.degrees(math.acos(d))
print format(e,'.1f')