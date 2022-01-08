from flask import request, json, Blueprint, jsonify, Response
from main.domain.dto.IncomeResultDto import IncomeResultDto
from src.main.service.IncomingService import IncomingService


class IncomingController():
    incoming_app = Blueprint('incoming_app', __name__, url_prefix='/')

    def __init__(self, incomingService : IncomingService):
        self.incomingService = incomingService
    
    def checkParameter(params):
        return len(params) == 0

    @incoming_app.route('/income/<id>', methods = ['POST'])
    def income(self,id):
        params = json.loads(request.get_data())

        if self.checkParameter(params):
            return jsonify({"result": False, "msg": "Wrong Params"})

        incomeResultDto = self.incomingService.incomeService(params)

        if not incomeResultDto.result:
            return Response(incomeResultDto.toJson, status=400, mimetype='application/json')

        return Response(incomeResultDto.toJson, status=200, mimetype='application/json')
        
    @incoming_app.route('/outcome/<id>', methods = ['GET'])
    def outcomeController(self,id):
        outcomeResultDto = self.incomingService.outcomeService(id)

        if not outcomeResultDto.result:
            return Response(outcomeResultDto.toJson, status=400, mimetype='application/json')

        return Response(outcomeResultDto.toJson, status=200, mimetype='application/json')
    
    @incoming_app.route('/incomes/<id>', methods = ['GET'])
    def imcomesController(self,id):
        incomesResultDto = self.incomingService.incomesService(id)
        return Response(incomesResultDto.toJson, status=200, mimetype='application/json')








