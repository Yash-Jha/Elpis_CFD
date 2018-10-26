from sklearn import linear_model
import pandas as pd
import math

import pickle

def estimate(magnitude, coords, density):
    model = pickle.load(open('kernel/RegressionModel_Iran','rb'))
    coords = coords.split(",")
    coords = [float(i) for i in coords]
    density = float(density)

    prediction = float(model.predict([[6.1,38.108,48.069]])[0])

    if(prediction < 0):
        return 0
    else:
        return math.floor(prediction*density)

"""
data2 = pd.read_csv('data4.5.csv',sep=',')
data = pd.DataFrame(columns=data2.columns)
for index, row in data2.iterrows():
    if(row['Magnitude'] < 7.5 and row['Country'].strip() == 'Iran'):
        data = data.append(row)
    
X_ = data['Magnitude']

X = []
for index, row in data.iterrows():
    X.append([float(row['Magnitude']),row['Lat'],row['Long']])
X = np.array(X)
Y = np.array(data['Effective Area'])

reg = linear_model.LinearRegression().fit(X,Y)
print(reg.score(X,Y))
#    print(reg.predict([[7]]))

pickle.dump(reg, open('RegressionModel_Iran','wb'))

y_test = reg.predict(X)

#print(reg.predict([[6.1,38.108,48.069]]))
"""
