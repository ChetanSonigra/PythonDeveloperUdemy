# documentation
# https://matplotlib.org/stable/index.html
# do plt.show() to show graph in vs code

import matplotlib.pyplot as plt

# following line allows us to view graphics by running them directly on the notebook
# %matplotlib inline

# we create a plot using plt.plot()
plt.plot()

# we plot a list of numbers
a = [1,3,5,6,7]
plt.plot(a)

# now we will create two lists x and y.
x = list(range(101))
y = [n**2 for n in x]
plt.plot(x,y)

# there is another way to create graphics in matplotlib using OO(object oriented) method.

# we create the chart using plt.subplots()
fig, ax = plt.subplots()   # fig is whole canvas where charts are shown. # ax is particular chart/axis
ax.plot(x,y)

# Let's see how workflow in a matplotlib looks like

# import and prepare library
import matplotlib.pyplot as plt
#%matplotlib inline

# prepare the data
x = list(range(101))
y = [number**2 for number in x]

# prepare the plot area(fig) and plot itself(ax) using plt.subplots()
fig, ax = plt.subplots()

# Add the data to the chart
ax.plot(x,y)

# Customize the plot by adding title to the plot and x and y axes
ax.set(title= "Accumulated earnings per day", xlabel= "Days", ylabel = "Earnings")

# save our plot using fig.savefig()
fig.savefig('python1/Day15/graph_accumulated_earnings.png')

# now let's look at scatter plot

# create a new dataset using numpy library
import numpy as np

x1 = np.linspace(0,100,20)
y1 = x1**2
print(x1,y1, sep='\n')

# create x vs y scatterplot
fig, ax = plt.subplots()

ax.scatter(x1,y1)

# now we visulize the sin function using np.sin(x)
fig, ax = plt.subplots()
x2 = np.linspace(-10,10,100)
y2 = np.sin(x2)
ax.scatter(x2,y2)

# now let's look another chart type - bar chart which usually associates numerical results with categorical variables.

# let's create a dictionary with 3 dishes and their prices.
food = {'Pizza': 14, 'Hamburger':11, 'Sandwich':17}

# we will create a bar chart where x axis is formed by dictionary keys.

fig,ax = plt.subplots()

ax.bar(food.keys(), food.values())

# set corresponding titles
ax.set(title= 'Food prices', xlabel='Food',ylabel='Prices')


# let's try with horizontal bar chart.
fig, ax = plt.subplots()
ax.barh(list(food.keys()),list(food.values()))
ax.set(title= 'Food prices', xlabel='Prices',ylabel='Food')

# we create a distribution of 1000 random values normally distributed.
x = np.random.randn(1000)
# we create the histogram
fig , ax = plt.subplots()
ax.hist(x)


# now let's look at more complex example. working with subplots,or figures containing several graphs.
# we create a fig with 4 subgraphs(2 per row)
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2, ncols=2,figsize=(10,5))


fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2, ncols=2,figsize=(10,5))
ax1.plot(x1,y1)
ax2.scatter(x2,y2)
ax3.bar(food.keys(),food.values())
ax4.hist(np.random.randn(1000))

# matplotlib has a set of various style available
# check available styles
plt.style.available

# we change the default style to seaborn-v0_8-whitegrid
plt.style.use('seaborn-v0_8-whitegrid')

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2, ncols=2,figsize=(10,5))
ax1.plot(x1,y1,color='#fcba03')
ax2.scatter(x2,y2,color='#fcba03')
ax3.bar(food.keys(),food.values(),color='#03c6fc')
ax4.hist(np.random.randn(1000),color='#fc0333')
