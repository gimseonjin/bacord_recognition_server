# python -m venv env
# env\Scripts\activate.bat
# pip install -r requirements
# python app.py

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)