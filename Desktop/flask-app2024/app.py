from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is my API running on Heroku!"

if __name__ == '__main__':
    app.run(debug=True)