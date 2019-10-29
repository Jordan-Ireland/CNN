score = {'user':0, 'comp':0}
past_choices = []
past_computer = []

hands = {1:'Rock', 2:'Paper', 3:'Scissors'}
    
def rps(user_choice, computer_choice):
    # Print the choices
    user_hand = hands[user_choice]
    computer_hand = hands[computer_choice]

    # While loop to play the game, breaks after one round currently

    if user_choice == computer_choice:
        score['user'] += 1
        score['comp'] += 1
    elif ((user_choice == 1 and computer_choice == 3) or
            (user_choice == 2 and computer_choice == 1) or
            (user_choice == 3 and computer_choice == 2)):
        score['user'] += 1
    else:
        score['comp'] += 1

    results = {'past_choices': past_choices, 'score': score, 'past_computer': past_computer}
    
    return results

def predict_winner(user_image, model):
    '''
    Take in image input of 300x300 pixels of rock,paper,scissors
    Use the model to predict if it was a rock,papper, or scissors
    Output the prediction, and output a random choice of rock/paper/scissor
    Decide the winner
    '''

    import random

    # Pull in the image and the model's prediction of it
    result = model.predict(user_image)
    user_choice = 0

    # Change encoded results to RPS
    if result[0][0] == 1:
        user_choice = 2
    elif result[0][1] == 1:
        user_choice = 1
    elif result[0][2] == 1:
        user_choice = 3
        
    past_choices.append(hands[user_choice])

    # Have computer choose a choice
    computer_choice = random.randint(1,3)
    
    past_computer.append(hands[computer_choice])

    # Run the rock paper scissors game
    return rps(user_choice, computer_choice)

