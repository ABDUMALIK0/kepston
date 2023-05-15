from django.conf import settings
from joblib import load
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import pandas as pd
import os
RESNET_MODEL_FILE = settings.BASE_DIR / 'data' / 'filter_model.joblib'

new_model = load(RESNET_MODEL_FILE)

height=200
width=400
channels=3
batch_size=80

#img_shape=(height, width, channels)
img_size=(height, width)


def scalar(img): # scale pixel between -1 and +1
        return img/127.5 - 1

def preprocess(data):
    IMAGE_ROOT = '/Users/malik/Desktop/mydjango/myproject/finalkepstonD/static/images/'+str(data)
    
    d = {'filepaths':IMAGE_ROOT, 'labels': 'none'}
    df = pd.DataFrame(data=d,index=[0])
    tvgen = ImageDataGenerator(preprocessing_function=scalar)
    valid = tvgen.flow_from_dataframe(df, x_col='filepaths', y_col='labels', target_size=img_size, class_mode='categorical', color_mode='rgb', shuffle=False, batch_size=batch_size)
    return valid
    

def predict_model(d):
    x = preprocess(d)
    new_dict = {0: 'fire', 1: 'smoke'}
    pred = new_model.predict(x, steps=1)
    
    return new_dict[np.argmax(pred[0])]

