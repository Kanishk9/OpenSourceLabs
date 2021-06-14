import pandas as pd

#Q1
x=pd.read_csv("/home/kanishk/Downloads/Automobile_data.csv - Automobile_data.csv.csv")
x.head()
x.tail()

#Q2
x.replace(['?'],['NaN'])
x.replace(['n.a'],['NaN'])

#Q3
volvo=x[x['company']=='volvo']
print(volvo)

#Q4
print(x['company'].value_counts())

#Q5
company = x.groupby('company')
price = company['price'].max()
print(price)

#Q6
avg_mil = company['company','average-mileage'].mean()
print(avg_mil)

#Q7
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845,17995,135925,71400]}
Car_Price_Data = pd.DataFrame.from_dict(Car_Price)

Car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141,80,182,160]}
Car_Horsepower_Data=pd.DataFrame.from_dict(Car_Horsepower)

merged=pd.merge(Car_Price_Data,Car_Horsepower_Data, on ='Company')
print(merged)