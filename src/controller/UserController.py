from _typeshed import Self
from flask import request, json, Blueprint, jsonify, Response
from src.service.UserService import UserService


class UserController():
    user_app = Blueprint('user_app', __name__, url_prefix='/')

    def __init__(self, userService : UserService):
        self.userService = userService
    
    @user_app.route('/login', methods=['POST'])
    def login(self):
        params = json.loads(request.get_data())

        if self.checkParameter(params):
            return jsonify({"result": False, "msg": "Wrong Params"})

        result = self.userService.loginService(params)

        return Response(result.toJson, status=201, mimetype='application/json')


    @user_app.route('/signup', methods=['POST'])
    def signpu(self):
        params = json.loads(request.get_data())

        if self.checkParameter(params):
            return jsonify({"result": False, "msg": "Wrong Params"})
        
        result = self.userService.signUpService(params)

        return Response(result.toJson, status=201, mimetype='application/json')

