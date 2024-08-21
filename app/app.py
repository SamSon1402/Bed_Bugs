import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load the pre-trained model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('path to model')

model = load_model()

# Define class names
class_names = ['ant_bite', 'bed_bugs', 'chiggers', 'fleas', 'mosquitos', 'no_bites', 'spiders', 'ticks']

def preprocess_image(image):
    # Resize the image to match the input size of your model
    img = image.resize((224, 224))
    # Convert the image to a numpy array
    img_array = np.array(img)
    # Normalize the image
    img_array = img_array / 255.0
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict(image):
    preprocessed_img = preprocess_image(image)
    predictions = model.predict(preprocessed_img)
    class_index = np.argmax(predictions[0])
    confidence = predictions[0][class_index]
    return class_names[class_index], confidence

# Streamlit app
st.title('Insect Bite Classifier')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    
    label, confidence = predict(image)
    
    st.write(f"Prediction: {label}")
    st.write(f"Confidence: {confidence:.2f}")

st.write("Note: This app uses a pre-trained model to classify insect bites and skin conditions. "
         "Always consult a medical professional for accurate diagnosis and treatment.")