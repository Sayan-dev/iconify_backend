
from flask import Blueprint,jsonify,request
from cassandra.query import SimpleStatement

from app.utils.responses import success,failure
from app.database.models.Prompt import Prompt
from app.modules.image import AiImage
import uuid


icons = Blueprint("icons", __name__, static_folder='/static')

@icons.get("/icon_name")
def get_icons():
    return success("name", "Misty" )


@icons.get('/data')
def get_data():
    try:

        return jsonify("data")
    except Exception as e:
        return str(e), 500
    

@icons.post('/generate')
def generate_icon():
    try:
        content = request.get_json()
        prompt = Prompt()
        generator = AiImage(content)
        image_url = generator.imageGenerator()
        id = prompt.addOne(content)
        return jsonify({'id':str(id), 'image_url': image_url}), 201
    
    except Exception as e:
        return str(e), 500