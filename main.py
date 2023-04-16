from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7TKRVBGOSdSODGJa/giphy.gif" width="500" height="500"> '


if __name__ == "__main__":
    app.run(debug=True)