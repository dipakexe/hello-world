from flask import Flask

app = Flask(__name__)

@app.route('/')
def greet():
    return "Hello, World! This is my first Flask app."

if __name__ == '__main__':
    app.run()
