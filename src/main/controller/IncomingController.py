from flask import request, json, Blueprint, jsonify, Response
from src.main.domain.dto.IncomeResultDto import IncomeResultDto
from src.main.domain.dto.OutcomeResultDto import OutcomeResultDto
from src.main.domain.dto.IncomesResultDto import IncomesResultDto
from src.main.Config import Config

c = Config()
incomingService = c.getIncomingService()

incoming_app = Blueprint('incoming_app', __name__, url_prefix='/')

def checkParameter(params):
    return len(params) == 0

@incoming_app.route('/income/<id>', methods = ['POST'])
def income(id):
    params = json.loads(request.get_data())
    if checkParameter(params):
        return jsonify({"result": False, "msg": "Wrong Params"})
    incomeResultDto:IncomeResultDto = incomingService.incomeService(id,params)
    if not incomeResultDto.result:
        return Response(json.dumps(incomeResultDto.toJSON()), status=400, mimetype='application/json')
    return Response(json.dumps(incomeResultDto.toJSON()), status=200, mimetype='application/json')
    
@incoming_app.route('/outcome/<id>', methods = ['GET'])
def outcome(id):
    outcomeResultDto:OutcomeResultDto = incomingService.outcomeService(id)
    if not outcomeResultDto.result:
        return Response(json.dumps(outcomeResultDto.toJSON()), status=400, mimetype='application/json')
    return Response(json.dumps(outcomeResultDto.toJSON()), status=200, mimetype='application/json')

@incoming_app.route('/incomes/<id>', methods = ['GET'])
def imcomes(id):
    incomesResultDto:IncomesResultDto = incomingService.incomesService(id)
    return Response(json.dumps(incomesResultDto.toJSON()), status=200, mimetype='application/json')




