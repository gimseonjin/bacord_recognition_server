# python -m venv env
# env\Scripts\activate.bat
# pip install -r requirements
# python app.py

from flask import Flask, json, render_template, request, redirect, url_for, jsonify, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS
from UserRepository import UserRepository
from ItemRepository import ItemRepository
from IncomingRepository import IncomingRepository
from RecodeRepository import RecordRepository
from src.domain.User import User
from src.domain.Incoming import Incoming
import pyzbar.pyzbar as pyzbar
import cv2
from datetime import datetime
import numpy as np

app = Flask(__name__)
CORS(app)

userRepository = UserRepository()
itemRepository = ItemRepository()
incomingRepository = IncomingRepository()
recordRepository = RecordRepository()

@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        f = request.files['file']
        f.save('static/uploads/' + secure_filename(f.filename))

        img = cv2.imread('static/uploads/' + secure_filename(f.filename))

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imwrite('static/uploads/grayscale.jpg', gray)
        kernel_sharpen_1 = np.array([[1,-2,1],[-2,5,-2],[1,-2,1]])

        f_image = cv2.filter2D(gray,-1,kernel_sharpen_1)

        cv2.imwrite('static/uploads/sharpen.jpg', f_image)

        ret, i = cv2.threshold(f_image, 50, 255, cv2.THRESH_BINARY)
        
        cv2.imwrite('static/uploads/grayIronMan.jpg', i)

        decorded = pyzbar.decode(i)
        value = decorded[0].data.decode('utf-8')
        print(value)
        value = value.replace('\u001d', '')
        count = 2
        di = ""
        lotNo = ""
        manufYm = ""
        useTmlmt = ""
        itemSeq = ""
        while count != len(value):
            if value[0:count] == "01":
                di = value[count:count+14]
                count = count+14
                print("di : {0}".format(di))
            elif value[count:count+2] == "10":
                lotNo = value[count+2:count+8]
                count = count + 8
                print("lotNo : {0}".format(lotNo))
            elif value[count:count+2] == "11":
                manufYm = value[count+2:count+8]
                count = count + 8
                print("manufYm : {0}".format(manufYm))
            elif value[count:count+2] == "17":
                useTmlmt = value[count+2:count+8]
                count = count + 8
                print("useTmlmt : {0}".format(useTmlmt))
            elif value[count:count+2] == "21":
                itemSeq = value[count+2:]
                print("itemSeq : {0}".format(itemSeq))
                count = len(value)
        item = itemRepository.read(itemSeq)
    return jsonify({"itemName" : item.name, "company" : item.company, "date_manufacture" : item.date_manufacture, "img" : item.img, "di" : di})


@app.route('/record/<userId>', methods = ['GET'])
def recordController(userId):
    return jsonify({"result" : recordRepository.readAll(userId)})


@app.route('/img/<id>', methods=['GET'])
def imgController(id):
    return send_file('img/'+id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)