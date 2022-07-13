# -*- coding: utf-8 -*-
"""
Created on Fri May 27 21:48:36 2022

@author: HARISUDHAN raw
"""
#python program to add a value in specific position
l=[]
n=int(input("Enter the length of list : "))
for i in range(n):
   l.append(int(input("Enter a value : "))) 
print("List = ",l)
o=int(input("Enter the element to be added : "))
u=int(input("Enter the position : "))

p=l[:u-1]+[o]+l[u-1:]
print("Final list = ",p)
