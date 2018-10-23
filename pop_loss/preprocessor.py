import pandas as pd
import numpy as np

df1 = pd.read_csv('data2.csv', error_bad_lines=False,sep=',')
df2 = pd.read_csv('API_EN.POP.DNST_DS2_en_csv_v2_10182003.csv', error_bad_lines=False,sep=',')

"""
for index, row in df1.iterrows():
    df1[index:index+1]['Country'] = row['Country'].strip()

df1.to_csv('data2.csv')
"""

s1 = df1['Country']
s2 = df2['Country Name']

ss1 = set(s1)
ss2 = set(s2)

count = 0

for i in ss1:
    for j in ss2:
        if(i == j):
            break
    else:
        print(i)
        count += 1

print(count)

#for index, row in df2.iterrows():
