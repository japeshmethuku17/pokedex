from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory, redirect, url_for, request, render_template
from pywebio.input import *
from pywebio.output import *

import sys
import os
import glob
import numpy as np
import cv2
import imutils

#app = Flask(__name__)

IMG_CATEGORIES = {0: 'Bulbasaur', 1: 'Charmander', 2: 'Jigglypuff', 3: 'Pidgeotto', 4: 'Pikachu', 5: 'Squirtle', 6: 'Togepi'}
IMG_SIZE = 299

MODEL_PATH = './models/xception-model.h5'
img_path = 'E:\\IRELAND\\GitHub\\pokemon-classification(copy)\\dataset\\dataset1\\pikachu\\00000001.jpg'
model = load_model(MODEL_PATH)

def upload():
	img_upload = file_upload(label= 'Upload image', multiple= False, accept= ['.jpeg', '.jpg', '.png'], placeholder='accepts images')
	print(img_upload.get('filename'))
	return img_upload

upload()
