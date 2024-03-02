# import libraries
import streamlit as st
import seaborn as sns

# Title
st.title('My first app')

# Header
st.header('IRIS')

# Subheader
st.subheader('Iris dataset')

# load iris dataset
df = sns.load_dataset('iris')

# Display the dataset
st.write(df)

# create bar chart
st.bar_chart(df['sepal_length'])

# create line chart
st.line_chart(df['sepal_length'])