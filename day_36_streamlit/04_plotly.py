# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# import data from plotly of gapminder
df = px.data.gapminder()
st.write(df)

# write columns name
st.write(df.columns)

# summary stat
st.write(df.describe())

# get list of unique years
year_options = df['year'].unique().tolist()
year = st.selectbox("Which year would you like to view?", year_options, 0)

# filter data by year
# df = df[df['year'] == year]

# plot data
fig = px.scatter(df, 
                 x='gdpPercap', 
                 y='lifeExp', 
                 size='pop', 
                 color='continent', 
                 hover_name='continent', 
                 log_x=True, 
                 size_max=60,
                 range_x=[100,100000],
                 range_y=[25,90],
                 animation_frame='year',
                 animation_group='country')


# update fig size
fig.update_layout(width=800, height=500)

st.write(fig)