#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 13:59:18 2019

@author: 005733815
"""
from lab1 import Employee 
import pickle
import os.path

filename = 'employees.dat'

def dictionary():
    
    if os.path.exists(filename):
        input_file = open(filename, 'rb')
        employee_file = pickle.load(input_file)
        input_file.close()
    else:
        employee_file = {}
        
    return employee_file 

def get_id(employee):
     ID = int(input('Employees ID number: \n'))
     return ID
 
def look_up(employee):
    ID = get_id(employee)
    
    if ID in employee :
        print ("found employee\n")
        print (employee [ID])
    else:
        print ("cannot find")

def add_new_employee(employee):
    #information = employee_information(employee)
    ID = get_id(employee)
    
    if ID not in employee:
        name = input('Enter employee name: ')
        department = input('Enter employee department: ')
        emp = Employee(name,ID,department)
        employee[ID]= emp.get_employee_name(),emp.get_employee_id(),emp.get_department()
        
        print("new employee added to list")
    else:
        print("give employee new id, that id is already taken")

def change_employee_information(employee):
    ID = get_id(employee)
   
    if ID in employee:
        print("found employee\n")
        print (employee [ID])
        print("would you like to change employee name")
        choice =int(input("(1 for yes) or (2 for no):"))
        if choice == 1:
            name = input('change employee name: \n')
            
        else:
            print("Employees name is the same \n")
            
        print ('would you like to change employee department: ')
        choice2 = int(input("(1 for yes) or (2 for no)"))
        if choice2 ==1 :
            department = input('change employee department: ')
        else:
            print("employees department is the same")
            
        new_employee = Employee(name,ID,department)
        employee[ID]= new_employee.get_employee_name(),new_employee.get_employee_id(),new_employee.get_department()
        
    else:
        print ("employee not found")
        
def delete_employee(employee):
    
    ID = get_id(employee)
    if ID in employee:
        delete_question = int(input ("are you sure you want to delete this person (1 for yes)(2 for no)"))
        if delete_question == 1: 
            del employee[ID]
            print("this employee is now deleted")
        else:
            print("cannot delete this employee ID not found")
    else: 
        print("employee not found")

def save_information(employee):
    save_file = open(filename,'wb')
    pickle.dump(employee,save_file)
    save_file.close()
    
def main():
    
    employee = dictionary()
    while True:
        print('-|---------------------------------|')
        print(' | 1. Look up an employee          |')
        print(' | 2. Add a new employee           |')
        print(' | 3. Change an existing employee  |')
        print(' | 4. Delete an employee           |')
        print(' | 0. Quit the program             |')
        print('-|---------------------------------|')
        option = int(input("option number: "))

        if option < 1 or option > 4:
            print ("not a valid choice")
        else:
            if option == 1:
                look_up(employee)
            elif option == 2:
                add_new_employee(employee)
            elif option == 3:
                change_employee_information(employee)
            elif option == 4:
                delete_employee(employee)
                
    save_information(employee)
    
main()              
     
        
            