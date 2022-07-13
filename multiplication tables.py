# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 19:25:37 2022

@author: HARISUDHAN
"""
print("PYTHON PROGRAM TO DISPLAY MULTIPLICATION TABLE")

n=int(input("Enter the number : "))
#defining function for multiplication table 
def tables(n):
    for i in range(1,11):
        print(n," *",i," =",n*i)
    print("Enter 1 to stop the program or enter 0 to continue multiplicatio")
    b=int(input("Enter your decision : "))
#applying condition whether to stop the program or to continue multiplying
    if(b==1):
        print("Program Has Ended")
        
    else:
        sl=11
        while(sl>0):
            print(n," *",sl,"=",n*sl)
            sl=sl+1
            
tables(n)