# import libraries
import streamlit as st
from PIL import Image

# add Title
st.write('''
# Add Media Web App
         ''')

# Add Image
img = Image.open('snow-leopard.jpg')
st.image(img, caption='Snow Leopard', use_column_width=True)

# Add Video
video_file = open('snow-leopard.mp4', 'rb')
st.video(video_file)
