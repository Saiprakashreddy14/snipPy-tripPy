# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 12:07:07 2019

@author: sai prakesh
"""


dict={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1,'m':1000,'d':500,'c':100,'l':50,'x':10,'v':5,'i':1}
sum,sum1=0,0
l=[]
n=input("enter the roman:")

for i in n:
    l.append(dict[i])
if((len(l))==1):
    sum=dict[n]
else:
    
    for i in range(len(l)-1):
        if(l[i]>=l[i+1]):
            sum=sum+l[i]
            print(sum)
        else:
            sum=sum+(l[i+1]-l[i])
            if(l[i+1]!=l[-1]):
                sum1=sum1+l[i+1]
            else:
                sum1=sum1
            print(sum,sum1)
    
    if(l[-1]<=l[-2]):
        sum=sum+l[-1]
        sum-sum1
print(sum)
