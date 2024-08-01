# -- coding: utf-8 --

from flask import Flask, render_template, Response
from keras.models import load_model
import tensorflow as tf
import cv2
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model
model1 = load_model(r'C:\\Users\\Admin\\Desktop\\25_3.h5')

# Function to predict on input image
def predict_image(image):
    # Resize the input image
    resized_img = cv2.resize(image, (224, 224))  
    input_img = resized_img / 255.0  # Normalize input images to [0, 1]
    input_img = np.expand_dims(input_img, axis=0)  # Add batch dimension
    # Make prediction
    predictions1 = model1.predict(input_img)
    pred = "REAL" if predictions1 >= 0.5 else "FAKE"
    return pred

# Function to capture video from webcam
def webcam_feed():
    # Initialize the camera
    camera = cv2.VideoCapture(0)  # Change the argument to 1, 2, etc., if you have multiple cameras
    while True:
        # Capture frame-by-frame
        ret, frame = camera.read()
        if not ret:
            break
        
        # Predict on the captured frame
        pred = predict_image(frame)
        
        # Display prediction result
        cv2.putText(frame, f'Prediction: {pred}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        # Convert frame to JPEG format
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # Release the camera
    camera.release()

# Route for accessing the webcam feed
@app.route('/')
def index():
    return render_template('redirectcamera.html')

# Route for streaming the webcam feed
@app.route('/video_feed')
def video_feed():
    return Response(webcam_feed(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(use_reloader=False)
