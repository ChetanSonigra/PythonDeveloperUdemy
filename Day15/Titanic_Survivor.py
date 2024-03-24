# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree
import os

path = os.getcwd()
df = pd.read_csv(f'{path}/python1/Day15/DataSet_Titanic.csv')

# display first 5 rows
df.head()

# store in variable X the predictor attributes (all the labels except "Survivor")
X = df.drop('Sobreviviente',axis=1) # 1 for column, 0 for row

# store in y the label to predict ("Survivor")
y = df.Sobreviviente

# display X
X.head()

# display y
y.head()

# We create a tree object
my_tree = DecisionTreeClassifier(max_depth=2,random_state=42)

# we train the machine
my_tree.fit(X,y)

# We predict on our set
prediction_y = my_tree.predict(X)

# We compare with the real labels
print("Accuracy: ", accuracy_score(prediction_y, y))

# we create a confusion matrix
confusion_matrix(y,prediction_y)

ConfusionMatrixDisplay(confusion_matrix(y,prediction_y)).plot()

ConfusionMatrixDisplay(confusion_matrix(y,prediction_y, normalize='true')).plot(cmap=plt.cm.Blues) # normalize

# we show a tree graphically
plt.figure(figsize=(10,8))
tree.plot_tree(my_tree,filled=True,feature_names=X.columns)
plt.show()

# try the same above process with depth=3

# we plot the importances in a bar chart
# we create the variables x (amounts) and y (columns)
relevance = my_tree.feature_importances_
columns = X.columns

df = pd.Series(relevance,index=columns)
# create the graph
sns.barplot(df)
plt.title('Relevance of each attribute')
plt.show()