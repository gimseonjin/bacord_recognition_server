# python -m venv env
# env\Scripts\activate.bat
# pip install -r requirements
# python app.py

from flask import Flask
from flask_cors import CORS
import src.main.controller.IncomingController as IncomingController
import src.main.controller.ItemController as ItemController
import src.main.controller.RecordController as ReconrdController
import src.main.controller.UserController as UserController
from src.main.Config import Config

app = Flask(__name__)
CORS(app)

c = Config()

app.register_blueprint(IncomingController.incoming_app)
app.register_blueprint(ItemController.item_app)
app.register_blueprint(ReconrdController.record_app)
app.register_blueprint(UserController.user_app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)