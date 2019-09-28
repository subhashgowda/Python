# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 19:47:23 2019

@author: subha
"""
#create excel using pandas
import pandas as pd

df1 = pd.DataFrame({'Data': ['a', 'b', 'c', 'd']})

df2 = pd.DataFrame({'Data': [1, 2, 3, 4]})

df3 = pd.DataFrame({'Data': [1.1, 1.2, 1.3, 1.4]})

writer = pd.ExcelWriter('multiple.xlsx', engine='xlsxwriter')

df1.to_excel(writer, sheet_name='HDD1')

df2.to_excel(writer, sheet_name='Sheetb')

df3.to_excel(writer, sheet_name='Sheetc')

writer.save()