#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 07:14:18 2023

@author: hasankilinc
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("eksikveriler.csv")

# Eksik veri var mı diye kontrol etmek
null_data = data.isnull()

for satir in range(len(null_data)):
    for sutun in range(len(null_data.columns)):
        if null_data.iloc[satir,sutun]:
            print(f"Satır :{satir} - Sütun :{sutun}")
   
            
            
# Eksik verilerden kurtulma
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")

yas = data.iloc[:,1:4].values                      # Yaş column'unu çekme

imputer = imputer.fit(yas[:,1:4])                  # imputer'a öğretme
yas[:,1:4] = imputer.transform(yas[:,1:4])         # Eksik değerleri değiştirme



# Kategorik Verileri İşleme - Sayısal değerlere çevirme
"""
Kategorik değişkenler 2 türdür: Nominal, Ordinal

Nominal : Hiçbir sırlaması olmayan değerler (Cinsiyet)
Ordinal : Sıralanabilir ama bu sıralama bir anlam ifade etmez (Plaka kodu)
"""
# Encoding kullanacağız
ulke = data.iloc[:,0:1].values                     # Ulke column'u çekme

from sklearn import preprocessing

# Label Encoding : Her bir değer için bir rakam atar
le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(data.iloc[:,0])

# One-Hot Encoding : Her bir değeri değişken yapar ve 1-0 değeri atar
ohe = preprocessing.OneHotEncoder()

ulke = ohe.fit_transform(ulke).toarray()



# Veri Birleştirme ve DataFrame Oluşturma
sonuc = pd.DataFrame(data=ulke, index= range(22), columns= ['fr', 'tr', 'us'])       # Ulke verisini DataFrame yapma

sonuc2 = pd.DataFrame(data= yas, index= range(22), columns= ['boy', 'kilo', 'yas'])  # Boy verisini DataFrame yapma

cinsiyet = data.iloc[:,-1].values

sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns= ['cinsiyet'])     # Cinsiyet verisini DataFrame yapma

s = pd.concat([sonuc, sonuc2], axis = 1)                                             # İki dataframe'i birleştirme

s2 = pd.concat([s, sonuc3], axis = 1)                                                # İki dataframe'i birleştirme





