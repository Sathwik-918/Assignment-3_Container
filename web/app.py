from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    with open('config.txt', 'r') as f:
        message = f.read().strip()
    return message

if __name__ == '__main__':
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
