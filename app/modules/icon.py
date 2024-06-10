
from flask import Blueprint
from app.utils.responses import success,failure

icons = Blueprint("icons", __name__, static_folder='/static')

@icons.get("/icon_name")
def get_icons():
    return success("name", "Misty" )
