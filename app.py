from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *

#from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import sys
import os
import glob
import numpy as np
import cv2
import imutils
from os.path import dirname, realpath, join


app = Flask(__name__)

IMG_CATEGORIES = {0: 'Bulbasaur', 1: 'Charmander', 2: 'Jigglypuff', 3: 'Pidgeotto', 4: 'Pikachu', 5: 'Squirtle', 6: 'Togepi'}
IMG_SIZE = 224

MODEL_PATH = './models/resnet-model.h5'

model = load_model(MODEL_PATH)

def predict_img():
	img_upload = file_upload(label= 'Upload image', multiple= False, accept= 'image/*', placeholder='Upload an image of pokemon', required= True)
	file_path = img_upload.get('filename')
	print(file_path)
	img = image.load_img(file_path, target_size = (IMG_SIZE, IMG_SIZE))
	x = image.img_to_array(img)
	pred = model.predict(np.expand_dims(x, axis=0))
	res = np.argmax(pred, axis = 1)
	im = open(file_path, 'rb').read()
	put_image(im, width= '400px', height= '400px')
	put_text("This pokemon is", IMG_CATEGORIES.get(int(res)))


app.add_url_rule('/tool', 'webio_view', webio_view(predict_img),
	methods=['GET', 'POST', 'OPTIONS'])

app.run(host='localhost', port=80)