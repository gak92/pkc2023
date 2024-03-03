# import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
# from pandas_profiling import profile_report
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# title
st.markdown('''
# EDA (Exploratory Data Analysis) Web App
''')

# how to upload file from pc
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader('Upload your input CSV file', type=['csv'])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown('''[Example CSV file]()''')

# profiling report
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        st.write('Using Example Dataset')
        @st.cache_data
        def load_csv():
            csv = sns.load_dataset('titanic')
            return csv
        df = load_csv()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)