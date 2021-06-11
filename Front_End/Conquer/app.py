from flask import *
from numpy import loadtxt
from keras.models import load_model
import os
from werkzeug.utils import secure_filename
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import joblib
model = joblib.load("D:/College/T.E/SEM-VI/ML/Project/Jupyterr/Models/random_forest.joblib")

# load model
# model = load_model('D:/College/T.E/SEM-VI/ML/Project/Jupyterr/Models/Exoplanets.h5')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html"
    )

#---------------------------------------------------#
# Following is the implementation of the model      #
#---------------------------------------------------#

@app.route('/predict', methods=['GET','POST'])
def predict():

    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        file_path = secure_filename(f.filename)
        f.save(file_path)
        # Make prediction
        df = pd.read_csv(file_path)
        l = np.array(df)
        print(l.shape)
        result = model.predict(l)
        unique, counts = np.unique(result, return_counts=True)
        final = dict(zip(unique, counts))
        os.remove(f.filename)
        return render_template('index.html', prediction_text1='Number of exoplanets Detected: {}'.format(final[1]), prediction_text2='Number of false positives: {}'.format(final[0]))

    return None

# random_list = ['koi_period', 'koi_period_err1', 'koi_period_err2', 'koi_time0bk', 'koi_time0bk_err1', 'koi_time0bk_err2', 'koi_impact', 'koi_impact_err1', 'koi_impact_err2', 'koi_duration', 'koi_duration_err1', 'koi_duration_err2', 'koi_depth', 'koi_depth_err1', 'koi_depth_err2', 'koi_prad', 'koi_prad_err1', 'koi_prad_err2', 'koi_teq', 'koi_insol', 'koi_insol_err1', 'koi_insol_err2', 'koi_model_snr', 'koi_steff', 'koi_steff_err1', 'koi_steff_err2', 'koi_slogg', 'koi_slogg_err1', 'koi_slogg_err2', 'koi_srad', 'koi_srad_err1', 'koi_srad_err2', 'ra', 'dec', 'koi_kepmag']