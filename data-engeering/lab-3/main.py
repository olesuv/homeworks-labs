import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
iris = pd.read_csv('iris.csv')
print(iris.head())
# create a figure and axis
fig, ax = plt.subplots()
# scatter the sepal_length against the sepal_width
ax.scatter(iris['sepal.length'], iris['sepal.width'])
# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')
plt.show()
# create color dictionary
colors = {'Setosa': 'r', 'Versicolor': 'g', 'Virginica': 'b'}
# create a figure and axis
fig, ax = plt.subplots()
# plot each data-point
for i in range(len(iris['sepal.length'])):
    ax.scatter(iris['sepal.length'][i],
               iris['sepal.width'][i], color=colors[iris['variety'][i]])
# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')
plt.show()
# get columns to plot
columns = iris.columns.drop(['variety'])
# create x data
x_data = range(0, iris.shape[0])
# create figure and axis
fig, ax = plt.subplots()
# plot each column
for column in columns:
    ax.plot(x_data, iris[column], label=column)
# set title and legend
ax.set_title('Iris Dataset')
ax.legend()
plt.show()
# pandas
iris.plot.scatter(x='sepal.length', y='sepal.width', title='Iris Dataset')
plt.show()
iris.drop(['variety'], axis=1).plot.line(title='Iris Dataset')
plt.show()
iris.plot.hist(subplots=True, layout=(2, 2), figsize=(10, 10), bins=20)
plt.show()
# seaborn
sns.scatterplot(x='sepal.length', y='sepal.width', data=iris)
plt.show()
sns.scatterplot(x='sepal.length', y='sepal.width', hue='variety', data=iris)
plt.show()
sns.lineplot(data=iris.drop(['variety'], axis=1))
plt.show()
iris_setosa = iris.loc[iris["variety"] == "Setosa"]
iris_virginica = iris.loc[iris["variety"] == "Virginica"]
iris_versicolor = iris.loc[iris["variety"] == "Versicolor"]
sns.FacetGrid(iris, hue="variety", height=3).map(
    sns.histplot, "petal.length").add_
legend()
sns.FacetGrid(iris, hue="variety", height=3).map(
    sns.histplot, "petal.width").add_l
egend()
sns.FacetGrid(iris, hue="variety", height=3).map(
    sns.histplot, "sepal.length").add_
legend()
sns.FacetGrid(iris, hue="variety", height=3).map(
    sns.histplot, "sepal.width").add_l
egend()
plt.show()
sns.boxplot(x="variety", y="petal.length", data=iris)
plt.show()
