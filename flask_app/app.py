from flask import Flask, render_template

app = Flask(__name__)

from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import PIL

test_model = ImageDataGenerator(rescale=1./255)

test = test_model.flow_from_directory(
    '../Rock-Paper-Scissors/test',
    target_size=(150,150),
    class_mode='categorical'    
)

json_file = open('../model.json','r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights('../20_epochs.h5')
print('Loaded Model from Disk')

loaded_model.compile(optimizer='rmsprop', loss='categorical_crossentropy',metrics=['accuracy'])

@app.route('/')
def home():
    score = loaded_model.evaluate(test,verbose=0)
    score_return = '%s: %.2f%%' % (loaded_model.metrics_names[1], score[1]*100)
    return render_template('home.html', data=score_return)


if __name__ == '__main__':
    app.run()