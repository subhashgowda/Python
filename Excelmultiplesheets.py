# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:34:28 2019

@author: subha
"""
#Create multiple excel sheets
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1,10):
        if i!=0:
                 j=i+2
                 
                
                 wb.create_sheet(index = j, title = 'HDD %d' %i)
                 wb.save(filename = "demo.xlsx")
                
       
        