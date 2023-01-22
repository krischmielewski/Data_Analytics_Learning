# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px  
from plotly.subplots import make_subplots
from datetime import datetime

house_df = pd.read_excel('/data/notebook_files/datasets/house.xls')

house_df2 = house_df.rename (columns=
{'Table 11 Housing market: simple average house prices, by new/other dwellings, type of buyer and  region, United Kingdom, from 1992 (quarterly) 1, 2, 3 (previously DCLG table 504)' : 'Region',
 'Unnamed: 1': 'Year',  
 'Unnamed: 2' : 'Quarter',
 'Unnamed: 4' : 'New dwellings',
 'Unnamed: 6' : 'Other dwellings',
 'Unnamed: 8' : 'All dwellings',
 'Unnamed: 10' : 'First time buyers',
 'Unnamed: 12' : 'Former owner occupiers',
 })

house_df2

columns = list(house_df2.columns)

columns

print("Missing values distribution:")
print(house_df2.isnull().mean())
print("")



house_df3 = house_df2.drop(columns=['Unnamed: 3','Unnamed: 5','Unnamed: 7','Unnamed: 9','Unnamed: 11','Quarter'])




house_df3 = house_df3.assign(Region=house_df3['Region'].shift(3))
house_df3['Year'] = house_df3['Year'].interpolate(method='pad', limit=3)

column_names = ('Year','New dwellings','Other dwellings','All dwellings','First time buyers','Former owner occupiers')

def covert_to_int(dataframe,name):
        return pd.to_numeric(dataframe[name],errors='coerce').fillna(0).astype(int)
        
for value in column_names:
    house_df3[value]=covert_to_int(house_df3,value)


#house_df3['Year']= pd.to_numeric(house_df3['Year'],errors='coerce').fillna(0).astype(int)
#house_df3['New dwellings']= pd.to_numeric(house_df3['New dwellings'],errors='coerce').fillna(0).astype(int)
#house_df3['Other dwellings']= pd.to_numeric(house_df3['Other dwellings'],errors='coerce').fillna(0).astype(int)
#house_df3['All dwellings']= pd.to_numeric(house_df3['All dwellings'],errors='coerce').fillna(0).astype(int)
#house_df3['First time buyers']= pd.to_numeric(house_df3['First time buyers'],errors='coerce').fillna(0).astype(int)


house_df3.drop(np.r_[0:7,2019:2032], inplace=True)

columns = ['Region','Year','New dwellings','Other dwellings','All dwellings','First time buyers','Former owner occupiers' ]

for column in columns:
    house_df3[column] = house_df3[column].fillna("")
    
    

house_df3

house_df3_United_Kingdom = house_df3.loc[0:128]
fig = plt.figure(figsize=(13,7), dpi=100, layout='constrained', facecolor='white', edgecolor='black', frameon=True)
ax = sns.barplot(data=house_df3_United_Kingdom, x='Year', y='New dwellings')
plt.title("United Kingdom - New dwellings", size=40)
plt.xlabel("Year", fontsize=25)
plt.ylabel("Price (£)", fontsize=25)
plt.yticks(ticks=[0,25000,50000,75000,100000,125000,150000,175000,200000,225000,250000,275000,300000,325000,350000])
plt.show()

house_df3_London = house_df3.loc[1267:1388]
fig = plt.figure(figsize=(13,7), dpi=100, layout='constrained', facecolor='white', edgecolor='black', frameon=True)
ax = sns.barplot(data=house_df3_London, x='Year', y='New dwellings')
plt.title("London - New dwellings", size=40)
plt.xlabel("Year", fontsize=25)
plt.ylabel("Price (£)", fontsize=25)
plt.yticks(ticks=[0,25000,50000,75000,100000,125000,150000,175000,200000,225000,250000,275000,300000,325000,350000,375000,400000,425000,450000,475000,500000])
plt.show()

house_df3_London = house_df3.loc[1267:1388]
fig = plt.figure(figsize=(13,7), dpi=100, layout='constrained', facecolor='white', edgecolor='black', frameon=True)
ax = sns.lineplot(data=house_df3_London)
plt.title("London - New dwellings", size=40)
plt.xlabel("Year", fontsize=25)
plt.ylabel("Price (£)", fontsize=25)
#plt.yticks(ticks=[0,25000,50000,75000,100000,125000,150000,175000,200000,225000,250000,275000,300000,325000,350000,375000,400000,425000,450000,475000,500000])
plt.show()

