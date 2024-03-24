# pandas is built on top of numpy and it is python's excel
# documentation: https://pandas.pydata.org/docs/
# importing pandas
import pandas as pd
import os

path = os.getcwd()


# we create a series of numbers and find its average
numbers = pd.Series([1,2,3,4,5,23,32])
print(numbers, numbers.sum(), numbers.mean(), sep = '\n')

# we create a series of 3 different colors
colors = pd.Series(['Red','Yellow','Green'])
print(colors)

# we create a series of type of cars
cars = pd.Series(['sedan', 'SUV','Pick-up'])
print(cars)

# combine the series of car type and colors to create a dataframe
car_table = pd.DataFrame({'Car Type': cars, 'Color': colors})
print(car_table)

# we connect the current notebook with our drive
# from google.colab import drive
# drive.mount("/content/drive")

#car_sales = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/car-sales.csv')
car_sales = pd.read_csv(f'{path}/python1/Day15/car-sales.csv')
print(car_sales)

# Export a dataframe as a csv to '/content/drive/MyDrive/Colab Notebooks/tests/' folder
# car_sales.to_csv('/content/drive/MyDrive/Colab Notebooks/this.csv')
car_sales.to_csv(f'{path}/python1/Day15/copy_sales.csv')

# let's analyze the data available in sales data
print(car_sales.dtypes)

# Let's apply descriptive statistics (number of values, mean, standard deviation, min, max values, quartiles)
print(car_sales.describe())

# we obtain information from datafram using info
print(car_sales.info())

# listing column names and length of car_sales
print(car_sales.columns, len(car_sales))

# Display the first 5/7 row of dataset
print(car_sales.head())
print(car_sales.head(7))
print(car_sales.tail())

# Use .loc to select index row 3 of the dataframe and .iloc to select row 3,5,7
print(car_sales.loc[3])
print(car_sales.iloc[[3,5,7]])

# select the mileage coloumn
print(car_sales['Mileage'])
# find the average value of column Mileage
print(car_sales['Mileage'].mean())

# select those columns that have values greater than 100,000 miles in mileage column
print(car_sales[car_sales['Mileage']>100000])

# create a double entry cross table between manufacturer and doors
print(pd.crosstab(car_sales['Manufacturer'],car_sales['Doors']))

# Group the columns by Manufacturer and look for the average value of numeric columns
print(car_sales.groupby(['Manufacturer']).mean(numeric_only=True))


# import matplotlib and create a chart with values of Mileage column
import matplotlib.pyplot as plt

print(car_sales['Mileage'].plot())

# more appropriate graph would be histogram
print(car_sales['Mileage'].hist())

# we try to plot the price column
# print(car_sales['Price (USD)'].plot())    -- gives error due to no numeric details
car_sales['Price (USD)'] = car_sales['Price (USD)'].str.replace('[\,\$\.]',"",regex= True)
car_sales['Price (USD)'] = car_sales['Price (USD)'].astype(int)/100
print(car_sales['Price (USD)'].plot())

# to show plots in vs code.
plt.plot(car_sales['Price (USD)'])
plt.show()