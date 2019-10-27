from flask import Flask, render_template
from PIL import Image
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
from functions import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


# Post method to run prediction model and return what each person/comp chose and who won
@app.route('/predict', methods=['POST'])
def predict():
    return predict_winner()

if __name__ == '__main__':
    app.run()