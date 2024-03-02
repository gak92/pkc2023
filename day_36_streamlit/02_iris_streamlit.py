# import libraries
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

# Heading
st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

# side bar
st.sidebar.header('User Input Parameters')

# Function to take user input
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

# Store the user input in a variable
df = user_input_features()

# Display the user input
st.subheader('User Input parameters')
st.write(df)

# Load iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target


rfc = RandomForestClassifier()
rfc.fit(X, y)

# Prediction
prediction = rfc.predict(df)
prediction_proba = rfc.predict_proba(df)

# Display the prediction
st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])

# Display the prediction probability
st.subheader('Prediction Probability')
st.write(prediction_proba)
