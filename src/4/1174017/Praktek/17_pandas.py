# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:54:44 2019

@author: ASUS
"""

import pandas

#Jawaban No. 3
def bukaModeListPandas():
    df = pandas.read_csv('teori.csv')
    print(df)

#Jawaban No. 4
def bukaModeDictPandas():
    df = pandas.read_csv('Book1.csv')
    dt = pandas.DataFrame.from_dict(df)
    print(dt)
    
#Jawaban No. 5
def ubahFormatTanggal():
    df = pandas.read_csv('Book1.csv', parse_dates=['tanggal lahir'])
    print(df)

#Jawaban No. 6
def ubahIndexKolom():
    df = pandas.read_csv('Book1.csv')
    df.index = ['Row_1', 'Row_2']
    print(df)

#Jawaban No. 7
def ubahNamaKolom():
    df = pandas.read_csv('Book1.csv')
    df.columns =['Col_1', 'Col_2', 'Col_3', 'Col_4'] 
    print(df)
    
def tulisCsvPandas():
    df = pandas.read_csv('Book1.csv', 
            index_col='NPM', 
            parse_dates=['Tanggal Lahir'],
            header=0, 
            names=['NPM', 'Nama', 'Kelas', 'Tanggal Lahir'])
    df.to_csv('Book5.csv')