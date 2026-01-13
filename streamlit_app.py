import pandas as pd
import streamlit as st
st.title('Welcome to the Streamlit App')

st.header('Personal Information', divider=True)

with st.sidebar:
    st.header('Personal Info')
    st.write('Do not leave any question blank')

st.markdown('This is the markdown')

name = st.text_input('Enter your name')
if name:
    st.write(f'Hello :blue[***{name}***]')

age = st.slider('Select your age', 0,100,0)
if age:
    st.write(f'You are {age} years old')

options = ['','Data Science', 'Data Analysis', 'Machine Learning']
choice = st.selectbox('Which is your preferred niche', options)
st.write(f'Your preferred niche is {choice}')

data = {
    'Name': ['John', 'Frank', 'Peter', 'Toni'],
    'age': [25, 30, 15, 32],
    'city': ['Lagos', 'NY', 'LA', 'California']
}
df = pd.DataFrame(data)
df.to_csv('sample_data.csv')
st.write('The biodata info')
st.write(df)

uploaded_file = st.file_uploader('Choose a CSV file', type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
