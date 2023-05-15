import streamlit as st
import requests

import numpy as np
import tensorflow
from PIL import Image
import os
import zipfile
import time

## Page configuration
st.set_page_config(
    page_title="Malaria Detection",
    page_icon="💾",
    layout="wide",
)
## Title bar
title = st.title("Malaria Detection[🔗](https://github.com/CaptaiN785/Maleria-detection)")
images = iter(os.listdir("images"))

for col in st.columns(4, gap="small"):
    img_name = next(images)
    col.image(os.path.join("images", img_name), width=250)
    img_class = str(img_name).replace("1", "").replace("2", "")
    img_class = img_class[: img_class.rfind(".")]
    col.text(img_class)


model_zip_link = "https://storage.googleapis.com/cushare-785.appspot.com/captain/2023-05-14%2010%3A34%3A39.414243%20Malaria%20detection%20Tensorflow%20model/model.zip"
model_path = "Model/model.zip"
main_model_path = "Model/model.hd5"
img_path = "Model/img.jpg"

if not os.path.exists(model_path):
    with st.spinner("Downloading model..."):
        data = requests.get(model_zip_link)
        with open(model_path, "wb") as file:
            file.write(data.content)
            st.balloons()

if not os.path.exists(main_model_path):
    with st.spinner("Extracting model..."):   
        zip = zipfile.ZipFile(model_path)
        zip.extractall("Model")
        zip.close()
        st.balloons()

## Defining the predict fuction
def Predict(image_path, model):
    label = {0:":red[Parasite]", 1:":green[Uninfected]"}

    img = Image.open(image_path).resize((96, 96), Image.LANCZOS)
    img = np.array(img)/255.0
    
    img = np.expand_dims(img, 0)
    # print("Shape of array is : ", img.shape)
    result = model.predict(img)
    return label[np.round(result[0][0])]

st.write(":green[Get [dataset](https://github.com/CaptaiN785/Maleria-detection/raw/main/Dataset.zip) to play with model or drag above image to Drag and Drop section.]")
file = st.file_uploader("Please upload cell image.")

if file is not None:
    with open(img_path, 'wb') as f:
        data = file.getvalue()
        f.write(data)
    
    try:
        with st.spinner("Loading model..."):
            model = tensorflow.keras.models.load_model(main_model_path)
            print("Model loaded successfully.")
            isModelLoaded = True
            st.success("Model loaded successfully", icon="🤖")

        cols = st.columns(3)
        cols[1].subheader(Predict(img_path, model))
        cols[1].image(img_path, "Uploaded image", width=300)

    except:
        print("Unable to load model.")
        st.error("Unable to load model")