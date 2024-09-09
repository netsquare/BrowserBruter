import os
import random
import cv2
import string
from PIL import Image, ImageDraw, ImageFont
from captcha.image import ImageCaptcha
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.utils import to_categorical
import requests

# Function to preprocess and predict text from a sample captcha
def predict_captcha(model, sample_captcha_path, label_to_int):
    # Load and preprocess the sample PNG captcha
    sample_captcha = cv2.imread(sample_captcha_path, cv2.IMREAD_GRAYSCALE)
    #sample_captcha = cv2.cvtColor(sample_captcha_image, cv2.COLOR_BGR2GRAY)
    sample_captcha = cv2.resize(sample_captcha, (28 * 4, 28))

    # Chop the sample captcha into four characters
    character_width = 28
    characters = [sample_captcha[:, i:i + character_width] for i in range(0, sample_captcha.shape[1], character_width)]

    # Preprocess each character and make predictions
    predicted_text = ""
    for char_image in characters:
        char_image = char_image.reshape((1, 28, 28, 1)).astype("float32") / 255.0
        predictions = model.predict(char_image)
        predicted_label_idx = np.argmax(predictions)
        predicted_label = list(label_to_int.keys())[list(label_to_int.values()).index(predicted_label_idx)]
        predicted_text += predicted_label

    return predicted_text

# Map labels to integers
label_to_int = {char: idx for idx, char in enumerate(string.ascii_letters + string.digits)}
num_classes = len(label_to_int)

# Load the saved model
model = tf.keras.models.load_model("res/samples/captcha_model.keras") # Change Here, Please provide correct path of the model
# Re-compile the model to ensure metrics are set
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

image_element = driver.find_element(By.ID, "captcha_image")
img_url = image_element.get_attribute('src')

response = requests.get(img_url)
with open('image.png', 'wb') as file:
	file.write(response.content)

# Example usage of the prediction function
#sample_captcha_path = "sample.png"  # Change this to the path of your sample captcha
predicted_text = predict_captcha(model, 'image.png', label_to_int)
print("Predicted Text:", predicted_text)

image_input_element = driver.find_element(By.ID, "captcha_input")

image_input_element.clear()
image_input_element.send_keys(predicted_text)




