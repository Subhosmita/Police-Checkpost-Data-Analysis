'''Here, we are going to analysis 
The data from a Police Check Post .'''

import pandas as pd
import numpy as np

# import the file
data=pd.read_csv("https://raw.githubusercontent.com/Subhosmita/Police-Checkpost-Data-Analysis/main/3.%20Police%20Data.csv")
#print(data.to_string())
df= print(data.head())

# we need some info about the data 
column= data.columns
print("the columns that are present = ",column)
info=data.info()
print(info)
# claning the data

nullcount= data.isnull().sum()
print(nullcount)

# drop the column which have highest null values
drop= data.drop(columns="country_name", inplace=True)
print("The new dataframe is = ",data)

#For Speeding , were Men or Women stopped more often ? 
count=data[data.violation== 'Speeding'].driver_gender.value_counts()
print("The count of men and women stopped = " ,count) # males stopped more often

#Does gender affect who gets searched during a stop ?
search= data.groupby('driver_gender').search_conducted.sum()
print(search)
count1=data.search_conducted.value_counts()
print(count1)

#What is the mean stop_duration ?
values= data.stop_duration.value_counts()
print(values)
# to find mean we need to change the datatype from str to int , we can use map func for that
#1st we find mean of every categories
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # for (0-15 min)
a_mean=np.mean(a)
print(a_mean)
b=[16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
b_mean=np.mean(b)
print(b_mean)
c=range(30,60)
c_mean=np.mean(c)
print(c_mean)

# mapping the data 
data['stop_duration']= data['stop_duration'].map( {'0-15 Min' : 8 ,  '16-30 Min' : 23 , '30+ Min' : 45 })
print(data)
st= data['stop_duration'].mean()
print("The mean vzalue = ",st)

#Compare the age distributions for each violation
gropu= data.groupby("violation").driver_age.describe()
print(gropu)
