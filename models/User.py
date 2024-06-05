from models.utils import generate_uuid


class User:
    def __init__(self, name):
        self.id = generate_uuid()
        self.name = name
