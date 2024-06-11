from app.database import database


class Base:
    """
    The base class model that extends to other models
    """
    def init_database(self, name:str) -> None:
        """
        Function for initialization of the databases
        """
        self.model = database[name]