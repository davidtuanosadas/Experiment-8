import pandas as pd
cars = pd.read_csv('cars.csv')
A=cars.iloc[:5,1:11:2]
B=cars[cars['Model']=='Mazda RX4']
C=cars.ix[cars['Model']=='Camaro Z28',['cyl']]
E=cars.loc[cars['Model']=='Mazda RX4 Wag',['cyl','gear']]
F=cars.loc[cars['Model']=='Ford Pantera L',['cyl','gear']]
G=cars.loc[cars['Model']=='Honda Civic',['cyl','gear']]
D=pd.concat([E,F,G])
print(A)
print(B)
print(C)
print(D)