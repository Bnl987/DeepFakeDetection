# -- coding: utf-8 --


from keras.models import load_model
import tensorflow as tf
import cv2
import numpy as np
import pandas as pd
model1 = load_model(r'C:\\Users\\Admin\\Desktop\\MAJOR PROJECT\\25_3.h5')



count = 0

ss = input("enter the file location: ")

img = cv2.imread(ss)
  # Skip if image not found
    
resized_img = cv2.resize(img, (224, 224))  # Adjust the resize dimensions to (224, 224)
input_img = resized_img / 255.0  # Normalize input images to [0, 1]
input_img = np.expand_dims(input_img, axis=0)  # Add batch dimension
    
predictions1 = model1.predict(input_img)


    
pred = "FAKE" if predictions1 >= 0.5 else "REAL"
print(f'The predicted class of the media is {pred}')


# Route for streaming the webcam feed
@app.route('/video_feed')
def video_feed():
    return Response(webcam_feed(), mimetype='multipart/x-mixed-replace; boundary=frame')

    
