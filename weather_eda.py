import pandas as pd
import numpy as np

df = pd.read_csv(r"E:\Git Folder\EDA_1\Project 1 - Weather Dataset.csv")
#print(df)
# It shows the first N rowa in the data 
#df.head()

# It shows the total no. of rows and no. of columns of the dataframe
df.shape

#The attribute provides the index of the dataframe
df.index

#It shows the name of each column
print(df.columns)

#It shows the data type of each column
print(df.dtypes)

#In a column it shows all the unique values. It can applied on a single column only. not on the whole dataframe
print(df["Weather"].unique())

#It shows total no of unique valyues in each column. It can be applied on a single column as well as whole dataframe
print(df.nunique()) #of whole dataset
print(df["Weather"].nunique()) #of particular column

# It shows total no. of non null in each column. It can be applied on a single column as well as on wole datafram
print(df.count())

#In a column, it shows all the unique values with their count. It can be applied on single column only
print(df["Weather"].value_counts())

# Provides the basic information about the dataframe
print(df.info())

#Q) 1. Find all the unique 'Wind Speed' values in the data.
print(df["Wind Speed_km/h"].unique())

#Q) 2. Find the number of times when the 'Weather is exactly Clear'.'
#1st Solution:
print(df["Weather"].value_counts())
#2nd Solution
print(df[df.Weather == "Clear"])
#3rd Solution
print(df.groupby("Weather").get_group("Clear"))

#Q) 3. Find the number of times when the 'Wind Speed was exactly 4 km/h'
print(df[df["Wind Speed_km/h"] == 4])

#Q. 4) Find out all the Null Values in the data.
#1st solution
print(df.isnull().sum())
#2nd Solution'
print(df.notnull().sum())

#Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'
df.head(2)
df.rename(columns= {"Weather": "Weather Condition"}, inplace=True)
print(df.columns)

#Q.6) What is the mean 'Visibility' ?
print(df.Visibility_km.mean())


#Q. 7) What is the Standard Deviation of 'Pressure' in this data?
print(df.Press_kPa.std())

#Q. 8) What is the Variance of 'Relative Humidity' in this data ?
print(df["Rel Hum_%"].var())

#Q. 9) Find all instances when 'Snow' was recorded.
#1st Solution:
print(df["Weather"].value_counts())
#2nd Solution
print(df[df["Weather"] == "Snow"])
#3rd Solution
print(df[df["Weather"].str.contains("Snow")])


#Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'
print(df[(df["Wind Speed_km/h"]>24) & (df["Visibility_km"]== 25)])

#Q. 11) What is the Mean value of each column against each 'Weather Condition' ?
print(df.groupby("Weather").mean(numeric_only=True))

#Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Condition' ?
print(df.groupby("Weather").min())
print(df.groupby("Weather").max())

#Q. 13) Show all the Records where Weather Condition is Fog
print(df[df.Weather == "Fog"])

#Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.
print(df[(df["Weather"]== "Clear") | (df["Visibility_km"]>40)])

#Q. 15) Find all instances when :¶
#A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
#or
#B. 'Visibility is above 40'
print(df[((df["Weather"] == "Clear") & (df["Rel Hum_%"] > 50)) | (df["Visibility_km"] > 40)])




