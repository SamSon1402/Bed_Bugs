# Insect Bite Classifier

This is a Streamlit app that uses a pre-trained deep learning model to classify images of insect bites and skin conditions.

## Features

- Upload an image of a suspected insect bite or skin condition.
- The app will classify the image and display the predicted label and confidence level.
- Supported classes: ant bites, bed bugs, chiggers, fleas, mosquitos, no bites, spiders, and ticks.
- Includes a disclaimer to consult a medical professional for accurate diagnosis and treatment.

## Requirements

- Python 3.7 or later
- Streamlit
- TensorFlow
- Pillow (PIL)
- NumPy

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/insect-bite-classifier.git
    ```

2. Install the required dependencies:

    ```bash
    pip install streamlit tensorflow pillow numpy
    ```

3. Place your pre-trained model file (in H5 format) in the `path/to/your/model.h5` location.

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

The app should now be running on `http://localhost:8501/`.

## Usage

1. Navigate to the web application in your browser.
2. Click the "Choose an image..." button to upload an image of a suspected insect bite or skin condition.
3. The app will classify the image and display the predicted label and confidence level.
4. The app includes a disclaimer to consult a medical professional for accurate diagnosis and treatment.

## Limitations

- This app uses a trained model, which may not be able to accurately classify all types of insect bites or skin conditions.
- The performance of the model may vary depending on the quality and diversity of the training data.
- The app is not a substitute for professional medical advice and should not be used for self-diagnosis or treatment.

## Future Improvements

- Expand the list of supported classes to cover a wider range of insect bites and skin conditions.
- Improve the model's accuracy and performance by fine-tuning or training a new model.
- Implement additional features, such as the ability to save classified images or provide more detailed information about each condition.
- Integrate the app with a medical database or API to provide more comprehensive information and guidance to users.

## Acknowledgments

This project was inspired by the need for a simple and accessible tool to help people identify and understand insect bites and skin conditions. The app uses a pre-trained deep learning model, and the developer would like to thank the researchers and engineers who contributed to the development of the underlying technology.
