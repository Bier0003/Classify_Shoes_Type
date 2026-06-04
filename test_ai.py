
from PIL import Image  
import numpy as np 
import tensorflow as tf

# open file
img = Image.open('uploads/test_pic.png')

# resize image to 224x224
img_resized = img.resize((224, 224))

print("resized picture size: ", img_resized.size)


img_color = img_resized.convert('RGB')

# convert image to array
img_array = np.array(img_color)
# preprocess the image for MobileNetV2
img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
# add batch dimension
img_array = np.expand_dims(img_array, axis=0)

print(" loading AI model...")
# load the pre-trained MobileNetV2 model with ImageNet weights
model = tf.keras.applications.MobileNetV2(weights='imagenet')

print (" AI model loaded, making prediction...")
predictions = model.predict(img_array)

# decode the predictionsto get human-readable labels
results = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0]

print(f"Predicted label: {results[0][1]} , with confidence: {results[0][2]:.2f}%)")