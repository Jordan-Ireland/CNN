from flask import Flask, render_template, request
from PIL import Image
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
from functions import *

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/play')
@app.route('/play', methods=['POST'])
# Post method to run prediction model and return what each person/comp chose and who won
def play():
    if(request.method == 'POST'):
        user_image = image.load_img(request.files['file'], target_size = (150,150))
        user_image = image.img_to_array(user_image)
        user_image = np.expand_dims(user_image, axis = 0)
        return render_template('play.html', predict=predict_winner(user_image))
    else:
        return render_template('play.html', predict=None)

if __name__ == '__main__':
    app.run()