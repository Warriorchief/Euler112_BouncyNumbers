#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:33:38 2017

@author: christophergreen
Bouncy numbers
Problem 112
Working from left-to-right if no digit is exceeded by the digit to its left it is called 
an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing 
number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy"
 number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the 
numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 
the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

def is_bouncy(x):
    drop=False
    rise=False
    s=str(x)
    i=0
    while i<len(s)-1:
        if s[i]<s[i+1]:
            rise=True
        if s[i+1]<s[i]:
            drop=True
        i+=1
    if rise and drop:
        #print(x,"is bouncy")
        return True
    else:
        #print(x,"is not bouncy")
        return False

def main(target):
    j=100
    bouncy_count=0
    bouncy_prop=0
    while bouncy_prop<target:
        if is_bouncy(j):
            bouncy_count+=1
            bouncy_prop=bouncy_count/j
        j+=1
    print("you reach the bouncy_prop",target,"at element",j-1)
    return 
    
#main(.9) #--> reached the bouncy_prop of 0.9 at the number 21780    
    
main(.99) # --> reached the bouncy_prop of 0.99 at the number 1587000 CORRECT

