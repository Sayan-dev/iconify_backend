from app.database.models.BaseModel import Base
from typing import Any, Dict, List

class Prompt(Base):

    def __init__(self):
        self.init_database('prompt')

    def addOne(self,data:Dict[str,Any]):
        info = {
            "business_type": data['business_type'],
            "look_and_feel": data['look_and_feel'],
            "text": data['text'],
            "tagline": data['tagline'],
            "colors": data['colors'] 

        }
        

        id = self.model.insert_one(info).inserted_id
        return id

