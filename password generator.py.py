# -*- coding: utf-8 -*-
"""
Created on Fri May 27 22:11:22 2022

@author: HARISUDHAN
"""
print("Please enter 5 or above number for strong passwords")
import random
import array

l=int(input("Enter the length of the password to be generated : "))
if(l<=4):
    print("Enter atleast 5 for generating password ")
else:
    digits=['0','1','2','3','4','5','6','7','8','9']
    lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    symb=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','+','/','<','>',':',';','?']

    cl=digits+lower+upper+symb

    r_digit=random.choice(digits)
    r_upper=random.choice(upper)
    r_lower=random.choice(lower)
    r_symb=random.choice(symb)

    t=r_digit+r_upper+r_lower+r_symb

    for x in range(l - 4):
        t=t+random.choice(cl)
        jt=array.array('u',t)
        random.shuffle(jt)
    password=""
    for x in jt:
        password=password+x
    print(password)
        
    
