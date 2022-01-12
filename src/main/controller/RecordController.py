from flask import request, json, Blueprint, jsonify, Response
from main.domain.dto.RecordResultDto import RecordResultDto
from src.main.service.RecordService import RecordService


class RecordController():
    record_app = Blueprint('record_app', __name__, url_prefix='/')

    def __init__(self, recordService : RecordService):
        self.recordService = recordService
    
    @record_app.route('/record/<userId>', methods = ['GET'])
    def recordController(self,userId):

        recordResultDto = self.recordService.recordService(userId)

        return Response(recordResultDto.toJson, status=200, mimetype='application/json')
        