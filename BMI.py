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
weight=float(raw_input("please input your weight(kg)"))
high=float(raw_input("please input your high numbers(M)"))
bmi=weight/(high*high)
print format(bmi,'.2f')
