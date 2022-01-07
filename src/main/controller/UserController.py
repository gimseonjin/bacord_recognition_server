from _typeshed import Self
from flask import request, json, Blueprint, jsonify, Response
from src.main.domain.dto.LoginResultDto import LoginResultDto
from src.main.domain.dto.SignUpResultDto import SignUpResultDto
from src.main.service.UserService import UserService


class UserController():
    user_app = Blueprint('user_app', __name__, url_prefix='/')

    def __init__(self, userService : UserService):
        self.userService = userService
    
    @user_app.route('/login', methods=['POST'])
    def login(self):
        params = json.loads(request.get_data())

        if self.checkParameter(params):
            return jsonify({"result": False, "msg": "Wrong Params"})

        loginResultDto = self.userService.loginService(params)

        if not loginResultDto.result:
            return Response(loginResultDto.toJson, status=400, mimetype='application/json')

        return Response(loginResultDto.toJson, status=201, mimetype='application/json')


    @user_app.route('/signup', methods=['POST'])
    def signpu(self):
        params = json.loads(request.get_data())

        if self.checkParameter(params):
            return jsonify({"result": False, "msg": "Wrong Params"})
        
        signUpResultDto = self.userService.signUpService(params)

        if not signUpResultDto.result:
            return Response(signUpResultDto.toJson, status=409, mimetype='application/json')

        return Response(signUpResultDto.toJson, status=201, mimetype='application/json')

