from flask import Flask, render_template, request
import random

app = Flask(__name__)

#Define game options
options = ["rock", "paper", "scissors"]

@app.route('/')
def home():
    print(f"Trying to render template: {app.jinja_env.get_template('index.html')}")
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice'].lower()
    computer_choice = random.choice(options)

    #determine winner
    if user_choice == computer_choice:
        winner = 'It\'s a tie!'
    elif user_choice == "rock" and computer_choice == "scissors":
        winner = "You win! Rock smashes scissors"
    elif user_choice == "paper" and computer_choice == "rock":
        winner = "You win! Paper covers rock"
    elif user_choice == "scissors" and computer_choice == "paper":
        winner = "Computer wins! Scissors cut paper"
    else:
        winner = "Computer wins! Computer chose " + computer_choice

    return render_template('result.html', user_choice=user_choice, computer_choice=computer_choice, winner=winner)

if __name__ == '__main__':
    app.run(debug=True)
