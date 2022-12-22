# First, install Streamlit if you haven't already:
#!pip install streamlit

# Next, import Streamlit and other necessary libraries:
import streamlit as st
import numpy as np
import pandas as pd

# Create a title for your GUI:
st.title('My Cute GUI')

# Add a header to your GUI:
st.header('Welcome to my cute GUI!')

# Add a text input field:
name = st.text_input('What is your name?')

# Add a button that, when clicked, will greet the user by name:
if st.button('Say hello'):
  st.write(f'Hello, {name}!')

# Add a checkbox that the user can select:
like_cats = st.checkbox('Do you like cats?')

# If the user likes cats, show them a cute cat image:
if like_cats:
  st.image('https://static.vecteezy.com/system/resources/previews/001/131/305/non_2x/scottish-purebred-cat-photo.jpg')

# Add a slider for the user to adjust:
age = st.slider('How old are you?', min_value=0, max_value=100)

# Display the user's age:
st.write(f'You are {age} years old.')
