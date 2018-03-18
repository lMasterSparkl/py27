#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john
#
# Created:     11/01/2018
# Copyright:   (c) john 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def fibonaqi(number):
    sum(0)=0
    sum(1)=1
    for i in range(2,number):
        sum(i)=sum(i-1)+sum(i-2)
    return sum(number)
user_input=input("please input the number of fibonaqi what you want")
fibonaqi_output=fibonaqi(user_input)
print fibonaqi_output