#AIT HADDOU Marwan
#marwan.aithaddou@edu.uca.ac.ma
#09 DEC 2022

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

#data source : https://www.macrotrends.net/cities/21891/casablanca/population

data = pd.read_csv("data.csv", sep='delimiter' ,header=None, encoding='utf8', engine='python', names=['colA'])
print(data)

Data=data.loc[11:,:]
d = [pd.DataFrame(Data[col].tolist()).add_prefix(col) for col in Data.columns]
df = pd.concat(d, axis=1)

#splite Data
df_new = df['colA0'].str.split(',', -1, expand=True).rename(columns={0:'Date', 1:'Population', 2:'AC'})

#splite date
df_new1 = df_new['Date'].str.split('-', -1, expand=True).rename(columns={0:'Y', 1:'M', 2:'D'})

Date = df_new['Date']
Year = df_new1['Y']
Population = df_new['Population']
Annual_Change = df_new['AC']

#Plotting
x = [eval(i) for i in Year]
y = [eval(i) for i in Population]
ac =[eval(i) for i in Annual_Change]
fig, axs = plt.subplots(2)
fig.suptitle('')
axs[0].set_title('Population of Casablanca 1951 - 2035')
axs[0].scatter(x, y, color="red")
plt.xlabel('Year')
axs[1].set_title('Annual Change %')
axs[1].plot(x, ac, color="green")
plt.show()