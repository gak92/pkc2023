# import libraries
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# create sections
header = st.container()
data_set = st.container()
features = st.container()
model_training = st.container()

# create header
with header:
    st.title('Welcome to my Titanic Streamlit App')
    st.text('In this project, I will be building a simple web app to predict the fare of passengers on the Titanic')

# load data
with data_set:
    st.header('Titanic Data Set')
    st.text('The following is the data set used in this project')
    st.text('The data set is available in the Seaborn library')
    df = sns.load_dataset('titanic')
    df = df.dropna()
    st.write(df.head(10))

    # create bar chart for sex column
    st.subheader('Bar Chart of Sex Column')
    st.bar_chart(df['sex'].value_counts())

    # create bar chart for class column
    st.subheader('Bar Chart of Class Column')
    st.bar_chart(df['class'].value_counts())

    # create bar chart for age column
    st.subheader('Bar Chart of Age Column')
    st.bar_chart(df['age'].value_counts())

# create features
with features:
    st.header('The Features')
    st.text('The following are the features used in this project')
    st.text('The features were extracted from the "Name" column of the data set')

    st.markdown('1. **Feature1** - This is the first feature')
    st.markdown('2. **Feature2** - This is the second feature')

# model training
with model_training:
    st.header('Model Training')
    st.text('The following is the model training section')
    st.text('The model used in this project is a simple logistic regression model')
    st.text('The model is trained on the following features: Sex and Age')

    # making column
    input, display = st.columns(2)

    # create input fields
    max_depth = input.slider('How many people do you know:', min_value=10, max_value=100, value=20, step=5)

# Number of estimators
n_estimators = input.selectbox('How many trees do you want:', options=[50, 100, 200, 300, 'No Limit'])

# list named of features
input.text(df.columns)

# user input features
input_feature = input.text_input('Enter the name of the feature:', 'age') 

# machine learning model
model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
if n_estimators == 'No Limit':
    model = RandomForestRegressor(max_depth=max_depth)
else:
    model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

# define X and y
X = df[[input_feature]]
y = df[['fare']]

# fit our model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# make predictions
y_pred = model.predict(X_test)

# model evaluation
display.subheader('Model Evaluation')
display.text('The following is the model evaluation section')


# display metrices
display.subheader('Mean Squared Error: ')
display.write(mean_squared_error(y_test, y_pred))
display.subheader('\nMean Absolute Error: ')
display.write(mean_absolute_error(y_test, y_pred))
display.subheader('\nR2 Score: ')
display.write(r2_score(y_test, y_pred))




