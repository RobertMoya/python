#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:07:58 2019

@author: 005733815
"""

#cse lab1

class Employee():
    def __init__(self,name,ID,department):
        self.__employee_name=name
        self.__employee_id = ID
        self.__department = department

    def set_employee_name(self,name):
        self.__employee_name = name

    def set_employee_id(self,ID):
        self.__employee_id = ID

    def set_department(self,department):
        self.__department = department
    
    def get_employee_name(self):
        return self.__employee_name

    def get_employee_id(self):
        return self.__employee_id

    def get_department (self):
        return self.__department

class ProductionWorker(Employee):
    
    def __init__(self,name,ID,department,shift,pay,):
        Employee.__init__(self,name,ID,department)
        self.__shift = shift
        self.__pay = pay
        
        
    def set_shift(self,shift):
        self.__shift = shift

    def set_pay(self,pay):
        self.__pay = pay
    
    def get_shift(self):
        
        if(self.__shift == 1 ):
            return "Day Shift"
        elif(self.__shift==2):
            return "Night Shift"
        else:
            return "No Shift"
        
    def get_pay(self):
        return self.__pay 
    
  
   
        
    
        
def main():
    name = input ("Employees name:")
    ID = input ("Employees ID:")
    department = input ("Employees Department:")
    shift = int (input("shift number:"))
    pay = input ("payroll:")
    
    employee = ProductionWorker(name, ID, department,0,pay)
    employee.set_shift(shift)
    
    
    print("|-----Employee information--")
    print("| Employee name:      |", employee.get_employee_name())
    print("| Employee ID:        |", employee.get_employee_id())
    print("| Employee department:|", employee.get_department())
    print("| Employee shift:     |", employee.get_shift())
    print("| Employee pay:       |", employee.get_pay())
    print("|---------------------------")
    
if __name__ == '__main__':
    main()