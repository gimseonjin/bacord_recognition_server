from flask import request, json, Blueprint, jsonify, Response, send_file, render_template
from werkzeug.utils import secure_filename
from main.domain.dto.ItemResultDto import ItemResultDto
from src.main.service.ItemService import ItemService


class ItemController():
    item_app = Blueprint('item_app', __name__, url_prefix='/')

    def __init__(self, itemService : ItemService):
        self.itemService = itemService
    
    def checkParameter(params):
        return len(params) == 0

    @item_app.route('/', methods=['GET', 'POST'])
    def hello(self):
        return render_template('index.html')

    @item_app.route('/upload', methods=['GET', 'POST'])
    def upload(self):
        f = request.files['file']
        f.save('static/uploads/' + secure_filename(f.filename))

        itemResultDto:ItemResultDto = self.itemService.uploadSerivce(f.filename)

        if not itemResultDto.result:
            return Response(itemResultDto.toJson, status=400, mimetype='application/json')
        
        return Response(itemResultDto.toJson, status=200, mimetype='application/json')


    @item_app.route('/img/<id>', methods=['GET'])
    def img(self,id):
        return send_file('img/'+id)