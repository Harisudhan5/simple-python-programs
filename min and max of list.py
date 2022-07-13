# -*- coding: utf-8 -*-
"""
Created on Thu May 26 21:47:44 2022

@author: HARISUDHAN
"""
#python program to find the largest and smallest number in a list
a=[]
num=int(input("Enter the range of list  : " ))
for i in range(5):
    a.append(int(input("Enter value = ")))
print("List = ",a)
p=max(a)
q=min(a)
print("Largest value = ",p)
print("Smallest value = ",q)


    