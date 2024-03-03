# import libraries
import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Title
st.write('''# Machine Learning Web App''')

# Sidebar with select box to select the dataset
dataset_name = st.sidebar.selectbox('Select Dataset', ('Iris', 'Breast Cancer', 'Wine'))

# Sidebar with select box to select the classifier
classifier_name = st.sidebar.selectbox('Select Classifier', ('KNN', 'SVM', 'Random Forest'))

# Function to get the dataset
def get_dataset(name):
    data = None
    if name == 'Iris':
        data = datasets.load_iris()
    elif name == 'Breast Cancer':
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_wine()
    x = data.data
    y = data.target
    return x, y

# call get_dataset function
X, y = get_dataset(dataset_name)

# write shpae of the dataset
st.write('Shape of the dataset:', X.shape)

# write number of classes
st.write('Number of classes:', len(np.unique(y)))

# define parameters of the classifier
def add_parameter_ui(clf_name):
    params = dict()
    if clf_name == 'KNN':
        K = st.sidebar.slider('K', 1, 15)
        params['K'] = K
    elif clf_name == 'SVM':
        C = st.sidebar.slider('C', 0.01, 10.0)
        params['C'] = C
    else:
        max_depth = st.sidebar.slider('max_depth', 2, 15)
        n_estimators = st.sidebar.slider('n_estimators', 1, 100)
        params['max_depth'] = max_depth
        params['n_estimators'] = n_estimators
    return params

# call add_parameter_ui function
params = add_parameter_ui(classifier_name)

# Function to get the classifier
def get_classifier(clf_name, params):
    clf = None
    if clf_name == 'KNN':
        clf = KNeighborsClassifier(n_neighbors=params['K'])
    elif clf_name == 'SVM':
        clf = SVC(C=params['C'])
    else:
        clf = RandomForestClassifier(n_estimators=params['n_estimators'], max_depth=params['max_depth'], random_state=123)
    return clf

# call get_classifier function
clf = get_classifier(classifier_name, params)

# Split the dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# Fit the model
clf.fit(X_train, y_train)

# Predict the test set
y_pred = clf.predict(X_test)

# Accuracy of the model
acc = accuracy_score(y_test, y_pred)
st.write(f'Classifier: {classifier_name}')
st.write(f'Accuracy: {acc}')

# Plot the dataset
pca = PCA(2)
X_projected = pca.fit_transform(X)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

fig = plt.figure()
plt.scatter(x1, x2, c=y, alpha=0.8, cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar()

# Show the plot
st.pyplot(fig)