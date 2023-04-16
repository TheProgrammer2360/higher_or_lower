from flask import Flask
import random
app = Flask(__name__)

RANDOM_NUMBER = random.randint(0, 9)


@app.route("/")
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7TKRVBGOSdSODGJa/giphy.gif" width="500" height="500"> '



@app.route("/<int:number>")
def take_a_guess(number):
    if number == RANDOM_NUMBER:
        # win
        value = '<h1 style="color:red;">You got me!</h1>' \
                '<img src="https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif" width="500" height="500">'
    elif number < RANDOM_NUMBER:
        # less than
        value = '<h1 style="color:red;">Too Low, try again</h1>' \
                '<img src="https://media.giphy.com/media/mhxZiXPbpF8QmtJe7Q/giphy.gif" width="500" height="500">'
    else:
        # greater than
        value = '<h1 style="color:purple;">Too high, try again</h1>' \
                '<img src="https://media.giphy.com/media/79eQOjPPrisR9B2zy6/giphy.gif" width="500" height="500">'
    return value

if __name__ == "__main__":
    app.run(debug=True)