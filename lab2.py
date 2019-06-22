#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:53:11 2018

@author: 005733815
"""
import math
import random as rand
def is_collide():
    circle_one_x = float(input("please enter plot point x for circle one:"))
    circle_one_y = float(input("please enter plot point x for circle one:"))
    circle_one_radius = float(input("please enter a number for radius of circle:"))
    circle_two_x = float(input("please enter plot point x for circle two:"))
    circle_two_y = float(input("please enter plot point x for circle two:"))
    circle_two_radius = float(input("please enter a number for a radius of circle:"))
    circle_one = (circle_one_x,circle_one_y,circle_one_radius)
    circle_two = (circle_two_x,circle_two_y,circle_two_radius )
    print (circle_one,circle_two)
    distance_between_circles = math.sqrt(((circle_two[0] - circle_one[0])**2)+((circle_two[1] - circle_one[1])**2))
    radius_sum= (circle_one_radius + circle_two_radius)
    if distance_between_circles < radius_sum:
        print(True)
    else:
        print(False)
        
def scramble_words():
    user_input= input("please enter a sentence that you would like to scramble:" )
    text_split = user_input.split() 
    for i in text_split:
      '''  if i > 3:
         '''   
def combine_list_into_dic():
    names = ['Alice','Bob','Cathy','Dan','Ed','Frank',
             'Gary','Helen','Irene','Jack','Kelly','Larry']
    ages= [18,21,18,18,19,20,20,19,19,19,22,19]            
    dictionary = {}
    dictionary= dict(zip(names,ages))
    print (dictionary)
    return dictionary
def people():
    dictionary = combine_list_into_dic()
    age_entered = int(input("please enter the age of person:"))
    
    for age in dictionary: 
        if dictionary[age] == age_entered:
            print (age)
        else:
            print("list is empty")
            break
            
def combine_list_into_set():
     names = ['Alice','Bob','Cathy','Dan','Ed','Frank',
             'Gary','Helen','Irene','Jack','Kelly','Larry']
     ages= [18,21,18,18,19,20,20,19,19,19,22,19]  
    
     print (list(set().union(names,ages)))
    
def main():
    combine_list_into_set()
main()