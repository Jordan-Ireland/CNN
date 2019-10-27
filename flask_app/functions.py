from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
import os
import numpy as np
import random


def image_input():
    # Currently imports random file from test folder
    folder = random.choice(os.listdir(r'C:/Users/John/Lambda/RPS/CNN/Rock-Paper-Scissors/test'))
    filename = random.choice(os.listdir(r'C:/Users/John/Lambda/RPS/CNN/Rock-Paper-Scissors/test/' + folder))
    img = image.load_img(r'C:/Users/John/Lambda/RPS/CNN/Rock-Paper-Scissors/test/' + folder + '/' + filename, target_size=(150, 150,))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return img


def rps(user_choice, computer_choice):

    score = {'user':0, 'comp':0}

    hands = {1:'Rock', 2:'Paper', 3:'Scissors'}

    # Print the choices
    user_hand = hands[user_choice]
    computer_hand = hands[computer_choice]
    print("User's image appears to be", user_hand)
    print("Computer's image appears to be", computer_hand)

    # While loop to play the game, breaks after one round currently
    while True:

        if user_choice == computer_choice:
            print("It's a tie!")
        elif ((user_choice == 1 and computer_choice == 3) or
              (user_choice == 2 and computer_choice == 1) or
              (user_choice == 3 and computer_choice == 2)):
            score['user'] += 1
            print('User wins!')
        else:
            score['comp'] += 1
            print('Computer wins!')
        print(score)
        return score
        break

    print('Final score:', score)


def predict_winner():
    '''
    Take in image input of 300x300 pixels of rock,paper,scissors
    Use the model to predict if it was a rock,papper, or scissors
    Output the prediction, and output a random choice of rock/paper/scissor
    Decide the winner
    '''
    # Load in the CNN model
    json_file = open('../model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # Load in the model weights
    loaded_model.load_weights('../20_epochs.h5')
    print('Loaded model from disk')

    # Compile the model
    loaded_model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    # Pull in the image and the model's prediction of it
    img = image_input()
    result = loaded_model.predict(img)
    print(result)
    user_choice = 0

    # Change encoded results to RPS
    if result[0][0] == 1:
        user_choice = 2
    elif result[0][1] == 1:
        user_choice = 1
    elif result[0][1] == 1:
        user_choice = 3
    
    print(user_choice)

    # Have computer choose a choice
    computer_choice = random.randint(1,3)

    # Run the rock paper scissors game
    rps(user_choice, computer_choice)

