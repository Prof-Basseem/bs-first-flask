# Import the Flask class from the flask package
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define the route to the home page
@app.route('/')
def home():
    return "Hello, My App is funny Matarial"

# Run the app
    
if __name__ == '__main__':
    app.run(debug=Tru)