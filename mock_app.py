from flask import Flask, json, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/v1/supply-info/manages/{date}", methods=["POST"])
def createService():
    return jsonify({"result": True})

@app.route("/api/v1/supply-info/manages", methods=["GET"])
def readService():
    return jsonify({"result": True})

@app.route("/api/v1/supply-info/manages/update/{suplyContStdmt}/{suplyContSeq}", methods=["PUT"])
def updateService():
    return jsonify({"result": True})

@app.route("/api/v1/supply-info/manages/update/{suplyContStdmt}", methods=["DELETE"])
def deleteAllService():
    return jsonify({"result": True})


@app.route("/api/v1/supply-info/manages/delete/{suplyContStdmt}/{suplyContSeq}", methods=["DELETE"])
def deleteOneService():
    return jsonify({"result": True})


if __name__ == '__main__':
    app.run(host='localhost', port=3000)