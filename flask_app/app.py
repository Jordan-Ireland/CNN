from flask import Flask, render_template
from PIL import Image
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
from functions import *

app = Flask(__name__)


@app.route('/')
def home():
    score = loaded_model.evaluate(test,verbose=0)
    score_return = '%s: %.2f%%' % (loaded_model.metrics_names[1], score[1]*100)
    return render_template('home.html', data=score_return)


# Post method to run prediction model and return what each person/comp chose and who won
@app.route('/predict', methods=['POST'])
def predict():
    return predict_winner()

if __name__ == '__main__':
    app.run()