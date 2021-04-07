import numpy as np
import tensorflow as tf
import cv2
from keras.models import load_model
from My_Model import create_model


model = create_model( 60 , 60 , 1 )
# model.summary()
model.load_weights('model_weights')

# Convert the model.
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model.
with open('model.tflite', 'wb') as f:
  f.write(tflite_model)

