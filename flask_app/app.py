from flask import Flask, render_template, request, url_for
from PIL import Image
from functions import predict_winner
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

loaded_model = None

@app.route('/play')
@app.route('/play', methods=['POST'])
# Post method to run prediction model and return what each person/comp chose and who won
def play():
    if loaded_model == None:
        with open('model.json', 'r') as f:
            model = model_from_json(f.read())

        # Load in the model weights
        model.load_weights('20_epochs.h5')


    if(request.method == 'POST'):
        user_image = image.load_img(request.files['file'], target_size = (150,150))
        user_image = image.img_to_array(user_image)
        user_image = np.expand_dims(user_image, axis = 0)
        return render_template('play.html', predict=predict_winner(user_image, model))
    else:
        return render_template('play.html', predict=None)

if __name__ == '__main__':
    app.run()