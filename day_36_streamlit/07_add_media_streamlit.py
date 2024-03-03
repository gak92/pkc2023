# import libraries
import streamlit as st
from PIL import Image

# add Title
st.write('''
# Add Media Web App
         ''')

# Add Image and slider to control size of image
st.write('Display Image')
width = st.slider('Select Image Size', 0, 700, 350)

img = Image.open('snow-leopard.jpg')

st.image(img, caption='Snow Leopard', width=width)

# Add Video and start after 5 sec
video_file = open('snow-leopard.mp4', 'rb')
st.video(video_file, start_time=5)
