#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john
#
# Created:     10/01/2018
# Copyright:   (c) john 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def fibonaqi(number):
    if number<=1:
        if number==0:
            return 0
        elif number==1:
            return 1
        else:
            return "error"
    else:
        a2=fibonaqi(number-1)
        a1=fibonaqi(number-2)
        a3=a1+a2
        return a3
user_input=input("please input the number of fibonaqi what you want")
fibonaqi_output=fibonaqi(user_input)
print fibonaqi_output


