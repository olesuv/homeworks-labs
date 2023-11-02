import pandas as pd
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('Wine.csv')

X = df.drop(columns=['Customer_Segment'])
Y = df['Customer_Segment']

print(X.head())
print(Y.head())
