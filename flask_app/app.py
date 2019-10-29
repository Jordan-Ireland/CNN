from flask import Flask, render_template, request, url_for
from functions import predict_winner
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploaded_images'
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','tiff'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/play')
@app.route('/play', methods=['POST'])
# Post method to run prediction model and return what each person/comp chose and who won
def play():
    try:
        model
    except:
        with open('model.json', 'r') as f:
            model = model_from_json(f.read())

        # Load in the model weights
        model.load_weights('20_epochs.h5')

        # Compile the model
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    if(request.method == 'POST'):
        if 'file' not in request.files:
            return render_template('play.html', predict=None)
        file = request.files['file']
        if file.filename == '':
            return render_template('play.html', predict=None)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            user_image = load_img(str(app.config['UPLOAD_FOLDER'] + '/' + filename), target_size = (150,150))
            user_image = img_to_array(user_image)
            user_image = np.expand_dims(user_image, axis = 0)
            
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return render_template('play.html', predict=predict_winner(user_image, model))
        
        
        
    else:
        return render_template('play.html', predict=None)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run()