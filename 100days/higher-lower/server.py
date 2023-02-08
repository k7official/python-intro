from flask import Flask
import random

app = Flask(__name__)
number = random.randint(0, 10)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src=https://media.giphy.com/media/Kehzyp9EFa2IYDte8P/giphy.gif>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src=https://media.giphy.com/media/l0zAiJHyg0fMA/giphy.gif>"
    elif guess < number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src=https://media.giphy.com/media/3og0IJXQEKwIdIEYpy/giphy.gif>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src=https://media.giphy.com/media/LScxdCeIZxPkXKvgHE/giphy.gif>"


if __name__ == "__main__":
    app.run(debug=True)